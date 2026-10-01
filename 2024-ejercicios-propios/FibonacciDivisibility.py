# Para cada M, avanzamos Fibonacci modulo M hasta encontrar F(i) % M == 0 con i > 0.
import sys
d = sys.stdin.read().split()
out = []
for m in map(int, d[1:1 + int(d[0])]):
    a, b, i = 1 % m, 1 % m, 1
    while a:
        a, b, i = b, (a + b) % m, i + 1
    out.append(str(i))
print(" ".join(out))
