
def emulate(instructions):
  # did we already run a specific instruction?
  previous = [False for _ in range(len(instructions))]

  acc, i = 0, 0
  while i < len(instructions):
    # infinite loop detected
    if previous[i]:
      return None

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

# keep flipping instructions until we find one that doesn't end up in an infinite loop
for i in range(len(instructions)):

  # we only care about jmp's and nop's
  if instructions[i][0] == "acc":
    continue

  # keep a copy of the original instruction
  original = instructions[i][0]

  if instructions[i][0] == "jmp":
    instructions[i][0] = "nop"
  elif instructions[i][0] == "nop":
    instructions[i][0] = "jmp"
  
  result = emulate(instructions)

  # we found code that runs
  if result != None:
    print(result)
    break

  # restore to original
  instructions[i][0] = original