adaptors = [0]

with open("input.txt", "r") as file:
  for line in file.readlines():
    adaptors.append(int(line))

adaptors.sort()

# memoization array
dp = [0 for _ in range(len(adaptors))]

def num_arrangements(arr, size):
  if size <= 2:
    return 1

  if dp[size - 1] != 0:
    return dp[size - 1]

  # you can always extend the last arrangement
  curr = num_arrangements(arr, size - 1)
  
  if arr[size - 1] - arr[size - 3] <= 3:
    curr += num_arrangements(arr, size - 2)
  if size >= 4 and arr[size - 1] - arr[size - 4] <= 3:
    curr += num_arrangements(arr, size - 3)

  dp[size - 1] = curr
  return curr

print(num_arrangements(adaptors, len(adaptors)))

# example with input:
# 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19

# 1
# 1

# 1, 4
#    1

# 1, 4, 5
#       1

# 1, 4, 5, 6                (1, 4, 5 + 6), (1, 4 + 6)
#          2                (1) +          (1)

# 1, 4, 5, 6, 7             (1, 4, 5, 6 + 7), (1, 4, 5 + 7), (1, 4 + 7)
#             4             (2) +             (1) +          (1)