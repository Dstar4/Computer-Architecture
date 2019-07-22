# Architecture

**[Architecture](#Architecture)**
- [Ram](##ram)

- [CPU-Words](##CPU-words)

- [CPU Registers](##cpu-registers)

- [CPU Instructions](##CPU-Instructions)

- [CPU Clock](##CPU-Clock)

- [Concurrency](##Concurrency)

- [System Bus](##System-Bus)

- [Caching](##Caching)

**[Binary, Decimal, and Hex](#binary,-decimal,-and-hex)**
- [Number Bases](##Number-Bases)


---

- Transistors
- Gates
- Digital Logic common operations performed by gates
    - AND, OR, NOT
    XOR, NOR, NAND
- Gates can be pit together into far more complex structures
    - ALU
    - CPUs

## Ram

- Random Access Memory
- Fast compared to hard drives
- A big array of bytes that you can access by index
- Each element in RAM can store one byte, and 8-bit number
- Larger, multi-byte values are stored in sequential address in RAM
- The CPU communicates with RAM via the memory but.

## CPU words

- Bytes of data are stored in RAM
- Larger 64-bit (8-byte) numbers, stored sequentially in RAM, that the CPU can operate on at once are called words
- The exact number of bytes per word depends on the architecture
    - 8 bytes for a 64-bit CPU
    - 4 bytes for a 32-bit CPU
    - 1 byte for an 8-bit CPU

## CPU Registers

**Registers store words that can be accessed at ultra-high-speed**

- Think of them like variables that the CPI has at its disposal
- Similar to RAM, except stored directly on the CPI so they are much faster
- There are limited number of them at your disposal, usually 8, 16, or 32, depending on the CPU
- They have fixed names. ex. R0, R1, or EAX, EBX, etc. depending on the CPU
- Many CPUs can only perform math operations on registers which must be loaded from RAM first. (The x86 family can often perform math on registers quickly, or RAM slowly.)

## CPU Instructions

- Also stored in RAM with other data
- Are actually just numbers
- Humans often use mnemonics to refer to the instruction in a human readable way
- The CPU keeps track of the address of the currently-ececuting instruction in a RAM and performs different actions based on the instruction found there
- The address of the currently-executing instruction is held in a special register called the program counter(PC)
- CPUs usually have a significant number of instructions, around 50-200

## CPU Clock

- The clock in a modern CPU triggers a few billion times per second
- Clock cycle rate is measured in Hz, KHz, MHz or GHz (billions of cycles per second)
- Each instruction takes one or more clock cycles to execute
- The faster the clock, the more instructions can execute per second

## Concurrency

**How the CPU does more than one thing at once**

- Each hardware component can only do one thing at once
- Duplicate the hardware components
- Multi-core CPUs
- Pipelining
- Timesharing

## System Bus

**How data is passed around from the CPU to RAM, and from the CPU to peripherals**

- Address Bus: carries the address in RAM we're interested in, or the peripheral ID we're interested in
- Data Bus: carries data to be transmitted to or from RAM or peripherals
- Control Bus: controls whether or not the CPU is talking to RAM or a peripheral
- The size or width of the bus is typically the number of bits a computer is advertised as having. A 64-bit CPU has a 64-but wide data bus, and usually a 64-bit wide address bus.

## Caching

- Access to RAM is relative slow
- Access to Registers is fast
- Middle ground? Cache.
- Closer to CPU
- Usually arranged in a level hierarchy
- Cache Miss means you're trying to access memory that's not yet in the cache
- Cache Hit means the memory you want is in the cache already


# Binary, Decimal, and Hex

## Number Bases

The number base refers to how many individual digits that number has.

- Decimal has 10 digits (0,1,2,3,4,5,6,7,8,9) so it is base 10.
- Binary has 2 digits (0,1) so it is base 2. A binary digit is called a bit for short.
- Hexadecimal has 16 digits (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) so it is base 16.
- Octal has 8 digits (0,1,2,3,4,5,6,7) so it is base 8. (Not frequently used)

Hexadecimal is often called "hex" for short.

## Terminology

- Byte: 8 bits. Max value: 255, FF hex. Min value 0.
- Nibble: 4 bits. Max value: 15 decimal, F hex. Min value 0.
- Octet: synonym for byte.

## The Octal Trap

Even though octal (base 8) is rarely used, you can specify octal numbers in many languages witha leading zero:

```js
int x = 12; // decimal
int y = 012; // octal, decimal value 10!
```

Don't pad decimal numbers with leading zeros
