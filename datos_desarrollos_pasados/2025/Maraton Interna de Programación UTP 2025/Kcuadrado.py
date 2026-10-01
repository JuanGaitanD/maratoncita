import sys

q = int(sys.stdin.readline())
Modulo = 10**18 + 3

for _ in range(q):
    k = int(sys.stdin.readline())

    sys.stdout.write(str((k ** 2) % Modulo) + '\n')  
    