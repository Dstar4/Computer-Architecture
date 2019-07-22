"""
Base 10 0-9

7
8
9
10      1 ten, and 0 ones
123     1 hundred 2 tens, and 3 ones   1 * 1000 + 2 * 10 + 3 * 1

Base 2 0-1 - Binary

0
1
10      2 in binary
11      3 in binary


Base 16 0-9, A-F

 8
 9
 A
 B
 C
 D
 F
10

Base 64 A-Z, a-z, 0-9, +, /

132 decimal         base 10
10000100 binary     base 2
85 hex              base 16

x = 12
y = x + 4

x = 0b101011
y = x + 0b10

"""

x = 0b101011
y = x + 10

print(x, y)
# Print x in binary
print("{:b} {}".format(x, y))

x = "1010110"
y = int(x, 2)
print(y)

"""


8s      base 10
|4s
||2s
|||1s
1234    base 2

1000s   base 2
|100s
||10s
||||1s
1101    base 2

1 * 1000 + 1 * 100 + 0 * 10 + 1 * 1


0b1101 == ?? decimal (base 10)
Go through digits and count how many numbers are in each place
8 + 4 + 1 == 13

0b10101011 == 171 decimal

128 + 32 + 8 + 2 + 1 == 171

17 decimal == ?? binary
16 +  == 17
0b10000 + 0b1 = 0b10001

0b1111 == 15
0xF    == 15

0b 1010 0100
0x  A    4
0b10100100 == 0xA4

0x     C    8
0b   1100  1000

0xC8 == 0b11001000

0b11111111 always a power of 2 minus 1

0b1111
0b10000

0b 1111 1111 == 255
0x   F    F
"""
