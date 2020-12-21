import math
import copy
from functools import reduce

def all_arrays_share_common(possible):
  for p1 in possible:
    for p2 in possible:
      if p1 == p2:
        continue

      valid = False

      for x in p2:
        if x in p1:
          valid = True
          break

      if not valid:
        return False

  return True

with open("input.txt", "r") as file:
  foods = []
  ingredients = set()
  allergens = set()

  # iterate over every line in a file
  for line in file.read().split("\n"):
    ingre, aller = line[:-1].split(" (contains ")

    ingre = ingre.split(" ")
    aller = aller.split(", ")

    ingredients |= set(ingre)
    allergens |= set(aller)
    foods.append((ingre, aller))

  impossible = { k: set() for k in ingredients }

  for ingre, aller in foods:
    for a in aller:
      for i in ingredients:
        if i not in ingre:
          #print(i, "cannot be", a)
          impossible[i].add(a)

  not_allergens = [k for k, v in impossible.items() if len(v) == len(allergens)]

  count = 0
  for ingre, aller in foods:
    for i in ingre:
      if i in not_allergens:
        count += 1

  print(count)