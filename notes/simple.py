import sys

PRINT_DANIEL = 1
HALT = 2
PRINT_NUM = 3
SAVE_REGISTER = 4
PRINT_REGISTER = 5

memory = [0]*128
register = [0] * 8      # 8 registers
pc = 0  # Program Counter, points to currently-executing instruction

running = True
if len(sys.argv) != 2:
    print(f"usage:{sys.argv[0]} filename")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        address = 0

        for line in f:
            num = line.split("#", 1)[0]

            if num.strip() == "":   # ignore comment-only lines
                continue

            memory[address] = int(num)
            address += 1

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)

while running:
    command = memory[pc]

    if command == PRINT_DANIEL:
        print("Daniel!")
        pc += 1

    elif command == PRINT_NUM:
        operand = memory[pc+1]
        print(operand)
        pc += 2

    elif command == HALT:
        running = False

    elif command == SAVE_REGISTER:
        value = memory[pc+1]
        regnum = memory[pc+2]
        register[regnum] = value
        pc += 3
    elif command == PRINT_REGISTER:
        regnum = memory[pc+1]
        print(register[regnum])
        pc += 2
    elif command == PUSH:
        registers[SP] -= 1              # decrement SP
        regnum = memory[pc + 1]         # get the register number operand
        value = registers[regnum]       # get the value from that register
        memory[registers[SP]] = value   # store that value in memory at the SP

    else:
        print(f"unknown instruction {command}")
        sys.exit(1)
