import math

with open("input.txt", "r") as file:
  earliest, busses = file.readlines()
  busses = [int(x) for x in busses.split(",") if x != "x"]

  mn, mnid = 99999999999, 0
  for x in busses:
    e = x - int(earliest) % x

    if e < mn:
      mn = e
      mnid = x

  print(mnid * mn)