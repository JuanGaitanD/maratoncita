# Celdas peligrosas: a distancia Chebyshev <= H de una S/B (prefijos 2D). Refugios validos: R/Y/A no peligrosos;
# BFS multi-fuente (4 dir) da la distancia a un refugio. BFS final de Y a A por mar seguro con distancia <= D.
import sys
from collections import deque
def main():
    data = sys.stdin.buffer.read().split()
    n, m, H, D = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    g = b"".join(data[4:4 + n])
    W = m + 1
    pre = [0] * ((n + 1) * W)
    for i in range(n):
        row = 0; base = (i + 1) * W; up = i * W
        for j in range(m):
            ch = g[i * m + j]
            if ch == 83 or ch == 66: row += 1
            pre[base + j + 1] = pre[up + j + 1] + row
    N = n * m
    danger = bytearray(N)
    for i in range(n):
        a, b = max(0, i - H), min(n, i + H + 1)
        ra, rb = a * W, b * W
        for j in range(m):
            c, d = max(0, j - H), min(m, j + H + 1)
            if pre[rb + d] - pre[ra + d] - pre[rb + c] + pre[ra + c]:
                danger[i * m + j] = 1
    INF = 1 << 30
    dist = [INF] * N
    q = deque()
    for v in range(N):
        if g[v] in b"RYA" and not danger[v]:
            dist[v] = 0; q.append(v)
    while q:
        v = q.popleft(); dv = dist[v] + 1
        if dv > D: continue
        i, j = divmod(v, m)
        for u, ok in ((v - m, i > 0), (v + m, i < n - 1), (v - 1, j > 0), (v + 1, j < m - 1)):
            if ok and dist[u] == INF:
                dist[u] = dv; q.append(u)
    s = g.index(b"Y")
    steps = [-1] * N; steps[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        if g[v] == 65:
            print(steps[v]); return
        i, j = divmod(v, m)
        for u, ok in ((v - m, i > 0), (v + m, i < n - 1), (v - 1, j > 0), (v + 1, j < m - 1)):
            if ok and steps[u] < 0 and not danger[u] and dist[u] <= D and g[u] in b".YA":
                steps[u] = steps[v] + 1; q.append(u)
    print("OSIDEO WILL DIE")
main()
