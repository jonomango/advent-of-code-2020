import string

required = [
  ["byr", lambda v: 1920 <= int(v) <= 2002],
  ["iyr", lambda v: 2010 <= int(v) <= 2020],
  ["eyr", lambda v: 2020 <= int(v) <= 2030],
  ["hgt", lambda v: (v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193) or (v[-2:] == "in" and 59 <= int(v[:-2]) <= 76)],
  ["hcl", lambda v: v[0] == "#" and all((x in string.hexdigits) for x in v[1:])],
  ["ecl", lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]],
  ["pid", lambda v: len(v) == 9 and v.isdigit()]
]

valid = 0

with open("input.txt", "r") as file:
  for line in file.read().split("\n\n"):
    
    # fields = [["ecl", "amb"], ["hgt", "64in"], ...]
    fields = [x.split(":") for x in line.replace("\n", " ").strip().split(" ")]

    # make sure every field is present
    if not all((f in [x for x, _ in fields]) for f, _ in required):
      continue

    invalid = False

    for field, verify in required:
      # find the value from fields list
      _, value = fields[[f for f, _ in fields].index(field)]

      # verify it
      if not verify(value):
        invalid = True

    if not invalid:
      valid += 1

  print(valid)