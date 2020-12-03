with open("input.txt", "r") as f:
  valid = 0

  for line in f.readlines():
    policy, password = line.split(": ")

    # the char in the policy
    c = policy[-1]

    # min and max
    mn, mx = [int(x) for x in policy[:-2].split("-")]

    count = password.count(c)
    if count >= mn and count <= mx:
      valid += 1

  print(valid)