import sys
from itertools import combinations
mx, my = map(int, sys.stdin.read().split())
P = [(x, y) for x in range(mx + 1) for y in range(my + 1)]
cnt = [0] * 4
for a, b, c in combinations(P, 3):
    cr = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if cr == 0: cnt[3] += 1; continue
    ds = []
    for p, q, r in ((a, b, c), (b, a, c), (c, a, b)):
        ds.append((q[0]-p[0])*(r[0]-p[0]) + (q[1]-p[1])*(r[1]-p[1]))
    m = min(ds)
    cnt[0 if m > 0 else 1 if m == 0 else 2] += 1
print("\n".join(map(str, cnt)))
