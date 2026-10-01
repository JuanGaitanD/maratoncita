# Entre dos instantes en que ambos estan quietos, cada uno usa una sola compania (distintas).
# Dijkstra denso sobre pares (u,v): (u,v)->(u',v') cuesta max(DX[u][u'],DY[v][v']) o al reves.
import sys
d = sys.stdin.read().split()
n, x, y = int(d[0]), int(d[1]), int(d[2]); INF = 1 << 60
def floyd(p, cnt):
    D = [[INF] * n for _ in range(n)]
    for i in range(n): D[i][i] = 0
    for i in range(cnt):
        u, v, w = int(d[p + 3 * i]) - 1, int(d[p + 3 * i + 1]) - 1, int(d[p + 3 * i + 2])
        if w < D[u][v]: D[u][v] = w
    for k in range(n):
        Dk = D[k]
        for Di in D:
            dik = Di[k]
            if dik < INF:
                for j in range(n):
                    t = dik + Dk[j]
                    if t < Di[j]: Di[j] = t
    return D
DX = floyd(3, x); DY = floyd(3 + 3 * x, y)
N = n * n
dist = [INF] * N; dist[0] = 0
done = [False] * N
while True:
    b = -1; bd = INF
    for i in range(N):
        if not done[i] and dist[i] < bd: bd = dist[i]; b = i
    if b == N - 1 or b < 0: break
    done[b] = True; u, v = divmod(b, n)
    DXu, DYu, DXv, DYv = DX[u], DY[u], DX[v], DY[v]
    for a in range(n):
        p, q = DXu[a], DYu[a]; base = a * n
        for c in range(n):
            w1 = p if p > DYv[c] else DYv[c]
            w2 = q if q > DXv[c] else DXv[c]
            t = bd + (w1 if w1 < w2 else w2)
            if t < dist[base + c]: dist[base + c] = t
print(dist[N - 1])
