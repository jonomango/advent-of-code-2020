nums = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    nums.append(int(line))

preamble = 25

for i in range(preamble, len(nums)):

  valid = False
  start = max(0, i - preamble)
  end = i

  # find two numbers that add up to num[i]
  for x in range(start, end):
    for y in range(start, end):
      if x == y:
        continue

      if nums[x] + nums[y] == nums[i]:
        valid = True

  # the first invalid num
  if not valid:
    print(nums[i])
    break