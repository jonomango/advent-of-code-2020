nums = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    nums.append(int(line))

preamble = 25
first_invalid = 0

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
    first_invalid = nums[i]
    break

for i in range(0, len(nums)):
  num = 0

  j = i

  # find a continuous range of numbers that are <= first_invalid
  while num < first_invalid:
    num += nums[j]
    j += 1
  
  if num == first_invalid:
    print(min(nums[i:j]) + max(nums[i:j]))
    break