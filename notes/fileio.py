import sys

print(sys.argv[0])
print(sys.argv[1])
try:
    with open(sys.argv[1]) as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print(f"{sys.argv[0]}:{sys.argv[1]} not found.")
    sys.exit(2)
