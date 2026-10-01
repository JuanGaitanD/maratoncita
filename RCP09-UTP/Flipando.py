# Planificacion en bosque minimizando sum w*C: se toma el grupo con mayor w/p y se pega detras del grupo de su
# padre (costo extra P_padre * W_hijo). Heap con borrado perezoso + Union-Find. Raiz virtual 0 con p = w = 0.
import sys, heapq
def main():
    d = sys.stdin.buffer.read().split()
    n = int(d[0])
    P = [0] + list(map(int, d[1:n + 1]))
    Wt = [0] + list(map(int, d[n + 1:2 * n + 1]))
    m = int(d[2 * n + 1])
    par = [0] * (n + 1)
    for i in range(m):
        par[int(d[2 * n + 2 + 2 * i])] = int(d[2 * n + 3 + 2 * i])
    cost = sum(P[i] * Wt[i] for i in range(1, n + 1))
    dsu = list(range(n + 1))
    dead = bytearray(n + 1)
    # clave entera exacta: -(floor(w * 2^64 / p) * 2^20 + v), un solo int compara mas rapido que una tupla
    h = [-(((Wt[i] << 64) // P[i]) << 20 | i) for i in range(1, n + 1)]
    heapq.heapify(h)
    pop, push = heapq.heappop, heapq.heappush
    while h:
        x = -pop(h); v = x & 1048575
        if dead[v] or x >> 20 != (Wt[v] << 64) // P[v]: continue  # entrada vieja
        dead[v] = 1
        u = par[v]
        while dsu[u] != u: dsu[u] = dsu[dsu[u]]; u = dsu[u]
        dsu[v] = u
        cost += P[u] * Wt[v]
        P[u] += P[v]; Wt[u] += Wt[v]
        if u: push(h, -(((Wt[u] << 64) // P[u]) << 20 | u))
    print(cost)
main()
