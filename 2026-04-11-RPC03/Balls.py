# Para cada r se resuelve la cuadratica en g: p*g^2 + (p(2r-1) - 2rq)*g + p(r^2-r) = 0.
import sys
from math import isqrt
p, q = map(int, sys.stdin.read().split())
ans = "impossible"
for r in range(1, 10 ** 6 + 1):
    b = p * (2 * r - 1) - 2 * r * q
    disc = b * b - 4 * p * p * (r * r - r)
    if disc < 0: continue
    s = isqrt(disc)
    if s * s != disc: continue
    num = -b + s
    if num % (2 * p) == 0 and num // (2 * p) >= r:
        ans = "%d %d" % (r, num // (2 * p)); break
print(ans)
