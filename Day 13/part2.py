from functools import reduce

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

with open("input.txt", "r") as file:
  _, busses = file.readlines()
  busses = busses.split(",")

  # https://brilliant.org/wiki/chinese-remainder-theorem/

  a, n = [], []

  for i in range(len(busses)):
    if busses[i] == "x":
      continue

    a.append(int(busses[i]) - i)
    n.append(int(busses[i]))

  N = reduce(lambda x, y: x * y, n, 1)
  y = [N // x for x in n]
  z = [modinv(i, m) for i, m in zip(y, n)]

  print(sum([i * j * k for i, j, k in zip(a, y, z)]) % N)