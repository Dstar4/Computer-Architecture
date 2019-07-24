"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 256
        self.reg = [0] * 8

    def load(self, file):
        """Load a program into memory."""
        address = 0
        program = []

        try:
            with open(file) as f:
                for line in f:
                    instruction = line.split("#", 1)[0].strip()
                    if len(instruction):
                        program.append(int(instruction, 2))

            for instruction in program:
                self.ram[address] = instruction
                address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    # MAR - Memory Address Register
    def ram_read(self, MAR):
        return self.ram[MAR]

    # MDR - Memory Data Register
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            # self.trace()
            curr_reg = self.ram[self.pc]

            # print(self.ram[curr_reg])
            opt_a = self.ram[self.pc + 1]
            opt_b = self.ram[self.pc + 2]
            if curr_reg == 0b00000001:
                # print("HLT")                      # HLT - Halt
                running = False

            elif curr_reg == 0b10000010:            # LDI - Set value of a register to an int
                # print("LDI")
                self.reg[opt_a] = opt_b
                self.pc += 3
                # print(self.pc)

            elif curr_reg == 0b01000111:            # PRN - Print numeric value stored in the given register
                # print("PRN")
                print(self.reg[opt_a])
                self.pc += 2
            elif curr_reg == 0b10100010:            # MUL - Multiply register 0 and register 1
                # print("MUL")
                self.alu("MUL", opt_a, opt_b)
                self.pc += 3

            else:
                print(f'Unknown command {curr_reg}')
                sys.exit(1)
