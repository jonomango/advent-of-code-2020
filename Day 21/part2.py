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

  impossible = { k: v for k, v in impossible.items() if len(v) != len(allergens) }
  ingredients = []
  
  while len(allergens) > 0:
    for k, v in impossible.items():
      if sum(x in allergens for x in v) != len(allergens) - 1:
        continue
    
      a = ""

      for x in allergens:
        if x not in v:
          a = x
          break

      ingredients.append((k, a))

      allergens &= v
      break

  ingredients.sort(key=lambda x: x[1])
  print(",".join(x for x, _ in ingredients))