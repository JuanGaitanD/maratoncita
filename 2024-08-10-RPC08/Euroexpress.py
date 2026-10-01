# Basta que la cara mayor (q,r) quepa en una restriccion (a<=b); entonces p=q=a, r=b.
import sys
d = sys.stdin.buffer.read().split()
n = int(d[0]); best = 0
for i in range(n):
    a, b = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    if a > b: a, b = b, a
    best = max(best, a * a * b)
print(best)
