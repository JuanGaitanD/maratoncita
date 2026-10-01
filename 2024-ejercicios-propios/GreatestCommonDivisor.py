# Euclides para el MCD; MCM = a / mcd * b.
import sys
from math import gcd
d = list(map(int, sys.stdin.read().split()))
out = []
for k in range(d[0]):
    a, b = d[1 + 2 * k], d[2 + 2 * k]
    g = gcd(a, b)
    out.append("(%d %d)" % (g, a // g * b))
print(" ".join(out))
