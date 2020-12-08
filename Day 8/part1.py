
def emulate(instructions):
  # did we already run a specific instruction?
  previous = [False for _ in range(len(instructions))]

  acc, i = 0, 0
  while i < len(instructions):
    # stop the infinite loop detected
    if previous[i]:
      break

    previous[i] = True
    instr, value = instructions[i]

    # emulate
    if instr == "acc":
      acc += value
    elif instr == "jmp":
      i += value
      continue

    i += 1
  
  return acc

instructions = []

with open("input.txt", "r") as file:
  for line in file.readlines():
    instructions.append([line[:3], int(line[4:])])

print(emulate(instructions))