"""CPU functionality."""
import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.reg[7] = 0xf4
        self.FL = 0b00000000  # Flags

    @property
    def sp(self):
        return self.reg[7]

    @sp.setter
    def sp(self, value):
        self.reg[7] = value

    # MAR - Memory Address Register
    def ram_read(self, MAR):
        return self.ram[MAR]

    # MDR - Memory Data Register
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

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

        elif op == "CMP":
            # FL bits: 00000LGE
            # L Less-than: during a CMP, set to 1 if registerA is less than registerB, zero otherwise.
            # G Greater-than: during a CMP, set to 1 if registerA is greater than registerB, zero otherwise.
            # E Equal: during a CMP, set to 1 if registerA is equal to registerB, zero otherwise.

            # print("here cmp")
            result = self.reg[reg_a] - self.reg[reg_b]
            if result == 0:  # reg_a == reg_b
                self.FL = 0b00000001
            else:
                self.FL = 0b00000000

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

        elif op == "AND":
            self.reg[reg_a] &= self.reg[reg_b]

        elif op == "OR":
            self.reg[reg_a] |= self.reg[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

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
        self.running = True

        def HLT():
            self.running = False

        def LDI():
            # print("here LDI")
            self.reg[op_a] = op_b

        def POP():
            self.reg[op_a] = self.ram[self.sp]
            self.sp += 1

        def PUSH():
            self.sp -= 1
            self.ram[self.sp] = self.reg[op_a]

        def ST():
            self.ram[op_a] = self.reg[op_b]

        def CALL():
            self.sp -= 1
            self.ram[self.sp] = self.ram[self.pc + 1]
            self.pc = self.reg[op_a]

        def RET():
            self.pc = self.ram[self.sp]
            self.sp += 1

        def JEQ():
            # print("here jeq")
            if self.FL == 0b00000001:
                ra = self.ram[self.pc+1]
                rv = self.reg[ra]
                self.pc = rv
            else:
                self.pc += 2

        def JNE():
            # print("JNE")
            if self.FL == 0b00000000:
                ra = self.ram[self.pc+1]
                self.pc = self.reg[ra]
            else:
                self.pc += 2

        def JMP():
            ra = self.ram[self.pc+1]
            self.pc = self.reg[ra]

        branch_table = {
            0b10100000: lambda: self.alu("ADD", op_a, op_b),
            0b10000010: LDI,
            0b10100010: lambda: self.alu("MUL", op_a, op_b),
            0b01000110: POP,
            0b01000111: lambda: print(self.reg[op_a]),
            0b01000101: PUSH,
            0b10000100: ST,
            0b01010000: CALL,
            0b00010001: RET,
            0b10100111: lambda: self.alu("CMP", op_a, op_b),
            0b01010100: JMP,
            0b01010101: JEQ,
            0b01010110: JNE,
            0b10101000: lambda: self.alu("AND", op_a, op_b),
            0b10101010: lambda: self.alu("OR", op_a, op_b),
        }

        while self.running:
            # self.trace()
            ir = self.ram[self.pc]
            op_count = (ir & 0b11000000) >> 6
            sets_pc = (ir & 0b00010000) >> 4
            op_a = self.ram[self.pc + 1]
            op_b = self.ram[self.pc + 2]
            cmd = branch_table.get(ir)
            if not cmd:
                sys.exit(f'End Program')
            cmd()
            if not sets_pc:
                self.pc += (op_count + 1)
