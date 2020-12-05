required = [
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid"
]

valid = 0

with open("input.txt", "r") as file:
  for line in file.read().split("\n\n"):
    
    # fields = [["ecl", "amb"], ["hgt", "64in"], ...]
    fields = [x.split(":") for x in line.replace("\n", " ").strip().split(" ")]

    # make sure every field is present
    if not all((f in [x for x, _ in fields]) for f in required):
      continue

    valid += 1

print(valid)