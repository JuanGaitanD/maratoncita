# Hay triangulo si cada lado es menor que la suma de los otros dos.
import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for k in range(d[0]):
    a, b, c = d[1 + 3 * k:4 + 3 * k]
    out.append("1" if a + b > c and a + c > b and b + c > a else "0")
print(" ".join(out))
