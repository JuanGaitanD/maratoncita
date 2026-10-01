# El bloque i tiene i terminos; se busca i con i(i-1)/2 < n <= i(i+1)/2 y k = n - i(i-1)/2 - 1.
import sys
from math import gcd, isqrt
n = int(sys.stdin.read())
i = (1 + isqrt(8 * n)) // 2 + 2
while i * (i - 1) // 2 >= n: i -= 1
k = n - i * (i - 1) // 2 - 1
if k == 0: print(i)
else:
    g = gcd(k, i); print(i, "%d/%d" % (k // g, i // g))
