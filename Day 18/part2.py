import math
import copy
from functools import reduce


def solve_equation_no_paren(eq):
  eq = eq.split(" * ")
  new_eq = []

  for i in range(len(eq)):
    eq[i] = sum(map(int, eq[i].split(" + ")))

  total = 1
  for x in eq:
    total *= x

  return total

def solve_equation(eq):
  stack = []
  i = len(eq) - 1

  while i >= 0:
    if eq[i] == ")":
      stack.append(i)
    elif eq[i] == "(":
      start, end = i, stack.pop() + 1

      sub = str(solve_equation_no_paren(eq[start + 1:end - 1]))
      eq = eq[:start] + sub + eq[end:]

      # relocate the end ptrs
      d = end - start - len(sub)
      for j in range(len(stack)):
        stack[j] -= d

    i -= 1

  return solve_equation_no_paren(eq)

with open("input.txt", "r") as file:
  equations = []

  # iterate over every line in a file
  for line in file.read().split("\n"):
    equations.append(line)

  print("solution:", sum([solve_equation(x) for x in equations]))