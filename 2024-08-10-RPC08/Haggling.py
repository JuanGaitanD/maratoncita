# k = cadena mas larga (siguiente inicio >= fin+1). Respuesta = corte minimo de vertices
# que toque todas las cadenas de largo k: flujo maximo en el DAG por capas, con nodos
# "cadena" por capa (ordenados por inicio) para que las aristas sean O(n).
import sys
from collections import deque
def main():
    d = sys.stdin.buffer.read().split()
    n = int(d[0])
    iv = sorted((int(d[1 + 2 * i]), int(d[2 + 2 * i])) for i in range(n))
    L = [1] * n; R = [1] * n
    for i in range(n):
        for j in range(n):
            if iv[j][1] + 1 <= iv[i][0] and L[j] + 1 > L[i]: L[i] = L[j] + 1
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if iv[j][0] >= iv[i][1] + 1 and R[j] + 1 > R[i]: R[i] = R[j] + 1
    k = max(L)
    layer = [[] for _ in range(k + 2)]
    for i in range(n):  # iv ya esta ordenado por inicio
        if L[i] + R[i] - 1 == k: layer[L[i]].append(i)
    V = 2 + 3 * n; INF = n + 1
    g = [[] for _ in range(V)]; to = []; cap = []
    def add(u, v, c):
        g[u].append(len(to)); to.append(v); cap.append(c)
        g[v].append(len(to)); to.append(u); cap.append(0)
    chain = {}
    for l in range(1, k + 1):
        lst = layer[l]
        for p, j in enumerate(lst):
            chain[j] = 2 + 2 * n + j
            add(chain[j], 2 + j, INF)
            if p + 1 < len(lst): add(chain[j], 2 + 2 * n + lst[p + 1], INF)
            add(2 + j, 2 + n + j, 1)
            if l == 1: add(0, 2 + j, 1)
            if l == k: add(2 + n + j, 1, 1)
    for l in range(1, k):
        nx = layer[l + 1]
        for i in layer[l]:
            b = iv[i][1] + 1
            for j in nx:  # primer j de la capa siguiente con inicio >= b
                if iv[j][0] >= b:
                    add(2 + n + i, chain[j], INF); break
    flow = 0
    while True:
        par = [-1] * V; par[0] = -2; dq = deque([0])
        while dq and par[1] == -1:
            u = dq.popleft()
            for e in g[u]:
                if cap[e] and par[to[e]] == -1:
                    par[to[e]] = e; dq.append(to[e])
        if par[1] == -1: break
        v = 1
        while v != 0:
            e = par[v]; cap[e] -= 1; cap[e ^ 1] += 1; v = to[e ^ 1]
        flow += 1
    print(flow)
main()
