# Grafo de nombres padre->hijo. La raiz debe ser el unico nombre que es padre y nunca hijo
# (si no hay, un nodo que alcance a todos); posible si desde ella se alcanzan todos los nombres.
import sys
def main():
    t = sys.stdin.read().split()
    n = int(t[0])
    idx, adj, child = {}, [], []
    def get(s):
        if s not in idx:
            idx[s] = len(adj); adj.append([]); child.append(False)
        return idx[s]
    for k in range(n):
        a = get(t[1 + 4 * k][:-1]); b = get(t[4 + 4 * k])
        adj[b].append(a); child[a] = True
    V = len(adj)
    roots = [v for v in range(V) if not child[v]]
    if len(roots) > 1:
        print("impossible"); return
    if roots:
        r = roots[0]
    else:  # ultimo nodo en terminar un DFS: si alguien alcanza a todos, es este
        seen = [False] * V; r = 0
        for s in range(V):
            if seen[s]: continue
            seen[s] = True; st = [(s, 0)]
            while st:
                v, i = st[-1]
                if i < len(adj[v]):
                    st[-1] = (v, i + 1); u = adj[v][i]
                    if not seen[u]: seen[u] = True; st.append((u, 0))
                else:
                    st.pop(); r = v
    seen = [False] * V; seen[r] = True; st = [r]; c = 1
    while st:
        v = st.pop()
        for u in adj[v]:
            if not seen[u]: seen[u] = True; c += 1; st.append(u)
    print("possible" if c == V else "impossible")
main()
