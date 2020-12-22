import math
import copy
from functools import reduce

# return True if p1 won the round
def simulate_round():
  return True

def play_game(p1, p2):
  prev = []

  while len(p1) != 0 and len(p2) != 0:
    # p1 instantly wins
    if (p1, p2) in prev:
      return True, p1

    prev += [(p1, p2)]

    c1, c2 = p1[0], p2[0]
    p1, p2 = p1[1:], p2[1:]

    # did p1 win
    p1_won = c1 > c2

    if len(p1) >= c1 and len(p2) >= c2:
      p1_won, _ = play_game(p1[:c1], p2[:c2])

    if p1_won:
      p1 += [c1, c2]
    else:
      p2 += [c2, c1]

  if len(p1) > 0:
    return True, p1
  else:
    return False, p2

with open("input.txt", "r") as file:
  p1, p2 = file.read().strip().split("\n\n")

  p1 = list(map(int, p1[10:].split("\n")))
  p2 = list(map(int, p2[10:].split("\n")))

  p1_won, winning_cards = play_game(p1, p2)

  print(p1_won, sum(x * (i + 1) for i, x in enumerate(winning_cards[::-1])))