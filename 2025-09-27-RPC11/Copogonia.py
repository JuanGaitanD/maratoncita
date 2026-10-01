# k <= 10: se prueban subconjuntos por DFS. La matriz de distancias se actualiza en O(n^2)
# al agregar cada via (u, v, w): d[i][j] = min(d[i][j], d[i][u]+w+d[v][j], d[i][v]+w+d[u][j]).
# Se poda en cuanto todos los pares quedan <= m o el costo supera el mejor.
import sys
from math import hypot
def main():
    t = sys.stdin.read().split()
    n, k, m = int(t[0]), int(t[1]), float(t[2])
    P = [(int(t[3 + 2 * i]), int(t[4 + 2 * i])) for i in range(n)]
    o = 3 + 2 * n
    R = [(int(t[o + 3 * i]) - 1, int(t[o + 3 * i + 1]) - 1, int(t[o + 3 * i + 2])) for i in range(k)]
    pre = [0.0]                                   # perimetro acumulado
    for i in range(n):
        pre.append(pre[-1] + hypot(P[i][0] - P[(i + 1) % n][0], P[i][1] - P[(i + 1) % n][1]))
    per = pre[n]
    d0 = [[min(abs(pre[i] - pre[j]), per - abs(pre[i] - pre[j])) for j in range(n)] for i in range(n)]
    best = [float("inf")]
    def add(d, u, v):
        w = hypot(P[u][0] - P[v][0], P[u][1] - P[v][1])
        du, dv = d[u], d[v]
        res = []
        for row in d:
            a = row[u] + w; b = row[v] + w
            res.append([min(x, a + y, b + z) for x, y, z in zip(row, dv, du)])
        return res
    def dfs(i, d, cost):
        if cost >= best[0]: return
        if max(map(max, d)) <= m + 1e-9:
            best[0] = cost; return
        if i == k: return
        dfs(i + 1, add(d, R[i][0], R[i][1]), cost + R[i][2])
        dfs(i + 1, d, cost)
    dfs(0, d0, 0)
    print(best[0])
main()
