# Respuesta = max_j a[j] - min(a[j-m..j]); minimo de ventana deslizante con deque.
import sys
from collections import deque
d = sys.stdin.buffer.read().split()
n, m = int(d[0]), int(d[1]); a = list(map(int, d[2:2 + n]))
q = deque(); best = 0
for j in range(n):
    while q and a[q[-1]] >= a[j]: q.pop()
    q.append(j)
    if q[0] < j - m: q.popleft()
    best = max(best, a[j] - a[q[0]])
print(best)
