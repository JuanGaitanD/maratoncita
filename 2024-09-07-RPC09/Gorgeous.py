# Factible(P) es monotono (quitar la 1a vuelta abarata todo). Para P fijo, desde el ultimo
# color hacia atras cada color toma el maximo ancho <= ancho del siguiente que le alcance.
import sys
from bisect import bisect_left
d = sys.stdin.buffer.read().split()
n, k = int(d[0]), int(d[1])
t = list(map(int, d[2:2 + n])); s = list(map(int, d[2 + n:2 + n + k]))
pre = [0] * (n + 1)
for i in range(n): pre[i + 1] = pre[i] + t[i]
def ok(P):
    R, W = P, P
    for c in range(k - 1, -1, -1):
        if R == 0: return True
        # menor inicio b >= R-W con pre[R]-pre[b] <= s[c]
        b = max(bisect_left(pre, pre[R] - s[c], 0, R + 1), R - W)
        W = R - b; R = b
        if W == 0: return False
    return R == 0
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi + 1) // 2
    if ok(mid): lo = mid
    else: hi = mid - 1
print(lo)
