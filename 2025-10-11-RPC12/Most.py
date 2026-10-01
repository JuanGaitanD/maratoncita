# Grafo serie-paralelo: se reducen vertices de grado 2 (serie) y aristas paralelas.
# Cada arista compuesta guarda (mejor camino u-v, mejor ciclo interno); paralelo: ciclo = P1+P2.
import sys
def main():
    data = sys.stdin.buffer.read().split()
    V, E = int(data[0]), int(data[1])
    NEG = -1 << 62
    adj = [dict() for _ in range(V + 1)]
    best = NEG
    def add(a, b, P, C):
        nonlocal best
        d = adj[a]
        if b in d:
            P2, C2 = d[b]
            C = max(C, C2, P + P2); P = max(P, P2)
            if C > best: best = C
        d[b] = (P, C); adj[b][a] = (P, C)
    for k in range(E):
        a, b, s = int(data[2 + 3 * k]), int(data[3 + 3 * k]), int(data[4 + 3 * k])
        add(a, b, s, NEG)
    st = [v for v in range(1, V + 1) if len(adj[v]) == 2]
    alive = V
    while st and alive > 2:
        w = st.pop()
        if len(adj[w]) != 2: continue
        (a, (Pa, Ca)), (b, (Pb, Cb)) = adj[w].items()
        adj[w] = {}; del adj[a][w]; del adj[b][w]; alive -= 1
        add(a, b, Pa + Pb, max(Ca, Cb))
        if len(adj[a]) == 2: st.append(a)
        if len(adj[b]) == 2: st.append(b)
    print(best)
main()
