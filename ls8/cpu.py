"""CPU functionality."""

import sys

ADD = 0b10100000
MUL = 0b10100010
LDI = 0b10000010
PRN = 0b01000111


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.branchtable = {
            PRN: self.handle_PRN,
            LDI: self.handle_LDI,
            MUL: self.handle_MUL
        }

    def handle_PRN(self, a, b):
        print(self.reg[a])
        self.pc += 2

    def handle_LDI(self, a, b):
        self.reg[a] = b
        self.pc += 3

    def handle_MUL(self, a, b):
        self.alu("MUL", a, b)
        self.pc += 3

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

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

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
            self.trace()
            ir = self.ram[self.pc]

            opt_a = self.ram_read(self.pc + 1)
            opt_b = self.ram_read(self.pc + 2)

            if ir in self.branchtable:
                self.branchtable[ir](opt_a, opt_b)

            elif ir == 0b00000001:
                running = False

            else:
                raise Exception(f'Unknown instruction {self.pc}   {ir}')
