# K veces: Dijkstra de S a D, y se eliminan las aristas del camino encontrado. El K-esimo camino es la respuesta.
import sys, heapq
def main():
    d = sys.stdin.buffer.read().split()
    n, m, K, S, D = map(int, d[:5])
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, w = int(d[5 + 3*i]), int(d[6 + 3*i]), int(d[7 + 3*i])
        adj[a].append((b, w, i)); adj[b].append((a, w, i))
    alive = [True] * m
    INF = float("inf")
    for _ in range(K):
        dist = [INF] * (n + 1); pv = [0] * (n + 1); pe = [-1] * (n + 1)
        dist[S] = 0; h = [(0, S)]
        while h:
            dv, v = heapq.heappop(h)
            if dv > dist[v]: continue
            if v == D: break
            for u, w, e in adj[v]:
                if alive[e] and dv + w < dist[u]:
                    dist[u] = dv + w; pv[u] = v; pe[u] = e
                    heapq.heappush(h, (dist[u], u))
        path = [D]; v = D
        while v != S:
            alive[pe[v]] = False; v = pv[v]; path.append(v)
    print(dist[D])
    print(" - ".join(map(str, reversed(path))))
main()
