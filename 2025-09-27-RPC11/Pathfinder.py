# BFS multi-fuente desde los lobos da la distancia de cada celda. Luego se activan celdas
# de mayor a menor distancia uniendolas con DSU; la respuesta es la distancia con la que
# (1,1) y (r,c) quedan conectados (maximo cuello de botella).
import sys
def main():
    data = sys.stdin.buffer.read().split()
    r, c = int(data[0]), int(data[1])
    g = b"".join(data[2:2 + r])
    N = r * c
    dist = [-1] * N
    q = [i for i in range(N) if g[i] == 87]   # 'W'
    for i in q: dist[i] = 0
    h = 0
    while h < len(q):
        u = q[h]; h += 1
        d = dist[u] + 1; y, x = divmod(u, c)
        if x > 0 and dist[u - 1] < 0: dist[u - 1] = d; q.append(u - 1)
        if x < c - 1 and dist[u + 1] < 0: dist[u + 1] = d; q.append(u + 1)
        if y > 0 and dist[u - c] < 0: dist[u - c] = d; q.append(u - c)
        if y < r - 1 and dist[u + c] < 0: dist[u + c] = d; q.append(u + c)
    par = list(range(N)); on = [False] * N
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for u in reversed(q):                   # q esta ordenada por distancia creciente
        if dist[u] == 0: break
        on[u] = True; y, x = divmod(u, c)
        for v, okv in ((u - 1, x > 0), (u + 1, x < c - 1), (u - c, y > 0), (u + c, y < r - 1)):
            if okv and on[v]:
                a, b = find(u), find(v)
                if a != b: par[a] = b
        if on[0] and on[N - 1] and find(0) == find(N - 1):
            print(dist[u]); return
main()
