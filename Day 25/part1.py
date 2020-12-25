import math
import copy
from functools import reduce


def bruteforce_loop_size(key):
  value, loop_size = 1, 0

  while value != key:
    value = (value * 7) % 20201227
    loop_size += 1

  return loop_size

def transform(loop_size, subject):
  value = 1

  for _ in range(loop_size):
    value = (value * subject) % 20201227

  return value

with open("input.txt", "r") as file:
  card_key, door_key = map(int, file.read().strip().split("\n"))
  card_loop = bruteforce_loop_size(card_key)

  print(transform(card_loop, door_key))