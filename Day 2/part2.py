with open("input.txt", "r") as f:
  valid = 0

  for line in f.readlines():
    policy, password = line[:-1].split(": ")

    # the char in the policy
    c = policy[-1]

    # valid positions
    pos1, pos2 = [int(x) for x in policy[:-2].split("-")]

    # are the letters present?
    valid1 = pos1 <= len(password) and password[pos1 - 1] == c
    valid2 = pos2 <= len(password) and password[pos2 - 1] == c

    if (not valid1 and not valid2) or (valid1 and valid2):
      continue

    valid += 1

  print(valid)