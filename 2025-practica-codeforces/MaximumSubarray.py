# Kadane: la mejor suma que termina en i es max(x, mejor_anterior + x). O(n).
import sys
d = list(map(int, sys.stdin.read().split()))
best, cur = d[1], 0
for x in d[1:1 + d[0]]:
    cur = max(cur, 0) + x
    best = max(best, cur)
print(best)
