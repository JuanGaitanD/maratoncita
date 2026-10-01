# Camino minimo desde 1 con pesos negativos (sin ciclos negativos): SPFA (Bellman-Ford con cola).
# Se imprimen las ciudades con distancia minima < 0.
import sys
from collections import deque
d = sys.stdin.buffer.read().split()
n, m = int(d[0]), int(d[1])
g = [[] for _ in range(n + 1)]
for i in range(m):
    s, e, t, w = int(d[2 + 4 * i]), int(d[3 + 4 * i]), d[4 + 4 * i], int(d[5 + 4 * i])
    g[s].append((e, -w if t == b"r" else w))
INF = float("inf")
dist = [INF] * (n + 1); dist[1] = 0
inq = [False] * (n + 1); inq[1] = True
q = deque([1])
while q:
    u = q.popleft(); inq[u] = False; du = dist[u]
    for v, w in g[u]:
        if du + w < dist[v]:
            dist[v] = du + w
            if not inq[v]:
                inq[v] = True; q.append(v)
res = [str(v) for v in range(1, n + 1) if dist[v] < 0]
if res:
    print("\n".join(res))
