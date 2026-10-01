# Las ciudades perdidas no tocan a las sobrevivientes, asi que el orden de ataque entre las
# sobrevivientes es el de la simulacion pura (heap por grado). Luego, en reversa con DSU,
# se cuenta cuantas ciudades atacadas seguian conectadas a NY en su momento; respuesta = eso + 1.
import sys, heapq
def main():
    d = sys.stdin.buffer.read().split()
    n, m = int(d[0]), int(d[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = int(d[2 + 2 * i]), int(d[3 + 2 * i]); adj[u].append(v); adj[v].append(u)
    deg = [len(a) for a in adj]; gone = [False] * (n + 1); order = []
    pq = [(-deg[i], i) for i in range(2, n + 1)]; heapq.heapify(pq)
    while pq:
        dd, v = heapq.heappop(pq)
        if gone[v] or -dd != deg[v]: continue
        gone[v] = True; order.append(v)
        for w in adj[v]:
            if not gone[w] and w != 1:
                deg[w] -= 1; heapq.heappush(pq, (-deg[w], w))
    par = list(range(n + 1))
    def find(x):
        r = x
        while par[r] != r: r = par[r]
        while par[x] != r: par[x], x = r, par[x]
        return r
    inn = [False] * (n + 1); inn[1] = True; days = 1
    for v in reversed(order):
        inn[v] = True
        for w in adj[v]:
            if inn[w]: par[find(w)] = find(v)
        if find(v) == find(1): days += 1
    print(days)
main()
