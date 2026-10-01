# Recolectar x_{L+1} en b (pos(b)=L) exige llegar a b con nivel L: la masa viene de nodos con
# pos L-1 por caminos sin otros nodos de pos L. Por cada nivel se arma el arbol virtual de
# A_{L-1} U A_L y se pasan mensajes (subida/bajada) con pesos alpha^{L+1}/(deg-1) por nodo
# intermedio; la masa que llega a b por cada direccion se guarda para el siguiente nivel.
import sys
MOD = 998244353
def main():
    v = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k, p, q = v[:5]
    posof = {x: i for i, x in enumerate(v[5:5 + m])}
    pos = [posof.get(x, -1) for x in v[5 + m:5 + m + n]]
    inv_n = pow(n, MOD - 2, MOD)
    if n == 1:
        print(1 if pos[0] == 0 else 0); return
    adj = [[] for _ in range(n)]
    o = 5 + m + n
    for i in range(n - 1):
        a, b = v[o + 2 * i] - 1, v[o + 2 * i + 1] - 1
        adj[a].append(b); adj[b].append(a)
    al = p * pow(q, MOD - 2, MOD) % MOD
    deg = [len(x) for x in adj]
    inv = [0] * (n + 1); inv[1] = 1
    for i in range(2, n + 1): inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD
    # arbol enraizado en 0
    par = [-1] * n; dep = [0] * n; order = [0]; tin = [0] * n
    seen = [False] * n; seen[0] = True
    st = [0]; order = []
    while st:
        u = st.pop(); tin[u] = len(order); order.append(u)
        for w in adj[u]:
            if not seen[w]: seen[w] = True; par[w] = u; dep[w] = dep[u] + 1; st.append(w)
    LOG = max(1, (n).bit_length())
    upt = [par[:]]
    upt[0][0] = 0
    for j in range(1, LOG):
        pr = upt[-1]; upt.append([pr[pr[x]] for x in range(n)])
    def jump(x, d):                                  # ancestro de x con profundidad d
        k2 = dep[x] - d; j = 0
        while k2:
            if k2 & 1: x = upt[j][x]
            k2 >>= 1; j += 1
        return x
    def lca(a, b):
        if dep[a] < dep[b]: a, b = b, a
        a = jump(a, dep[b])
        if a == b: return a
        for j in range(LOG - 1, -1, -1):
            if upt[j][a] != upt[j][b]: a = upt[j][a]; b = upt[j][b]
        return par[a]
    Q = [1] * n; Qi = [1] * n                        # productos de 1/(deg-1) y (deg-1) desde la raiz
    for u in order[1:]:
        Q[u] = Q[par[u]] * inv[deg[u] - 1] % MOD; Qi[u] = Qi[par[u]] * (deg[u] - 1) % MOD
    groups = {}
    for x in range(n):
        if pos[x] >= 0: groups.setdefault(pos[x], []).append(x)

    def run(nodes, vpar, ew, sink, pw, emit):
        # nodes en preorden; devuelve {sink: [(vecino virtual, masa)]}
        S = {x: 0 for x in nodes}; up = {}; down = {}
        for x in reversed(nodes[1:]):
            val = emit(x, vpar[x])
            if not sink(x): val += pw(x) * S[x]
            up[x] = val % MOD * ew[x] % MOD
            S[vpar[x]] += up[x]
        down[nodes[0]] = 0
        for x in nodes[1:]:
            u = vpar[x]
            val = emit(u, x)
            if not sink(u): val += pw(u) * ((S[u] - up[x] + down[u]) % MOD)
            down[x] = val % MOD * ew[x] % MOD
        res = {}
        for x in nodes:
            if sink(x):
                lst = [(x if False else vpar[x], down[x])] if x != nodes[0] else []
                res[x] = lst
        for x in nodes[1:]:
            if sink(vpar[x]): res[vpar[x]].append((x, up[x]))
        return res

    ans = 0
    A0 = set(groups.get(0, []))
    # nivel 0: todo el arbol, cada nodo fuera de A0 es inicio posible
    e0 = [0 if x in A0 else inv_n * al % MOD * inv[deg[x]] % MOD for x in range(n)]
    r = run(order, par, [1] * n, lambda x: x in A0, lambda x: al * inv[deg[x] - 1] % MOD,
            lambda x, y: e0[x])
    H = {}
    for b, lst in r.items():
        H[b] = {"s": inv_n}
        for nb, ms in lst: H[b][nb] = (H[b].get(nb, 0) + ms) % MOD
    L = 0
    while H:
        ans = (ans + sum(sum(h.values()) for h in H.values())) % MOD
        L += 1
        if L not in groups: break
        f = pow(al, L + 1, MOD)
        sub = {}; tot = {}
        for b, h in H.items():
            sb = {}
            for d, ms in h.items():
                c = deg[b] if d == "s" else deg[b] - 1
                sb[d] = ms * f % MOD * inv[c] % MOD
            sub[b] = sb; tot[b] = sum(sb.values()) % MOD
        sinks = set(groups[L])
        pts = sorted(set(H) | sinks, key=lambda x: tin[x])
        allp = set(pts)
        for i in range(len(pts) - 1): allp.add(lca(pts[i], pts[i + 1]))
        nodes = sorted(allp, key=lambda x: tin[x])
        vpar = {}; ew = {}; stk = []
        for x in nodes:
            while stk and lca(stk[-1], x) != stk[-1]: stk.pop()
            if stk:
                u = stk[-1]; vpar[x] = u
                cnt = dep[x] - dep[u] - 1
                ew[x] = pow(f, cnt, MOD) * Q[par[x]] % MOD * Qi[u] % MOD
            stk.append(x)
        def realdir(u, y):
            return par[u] if vpar.get(u) == y else jump(y, dep[u] + 1)
        def emit(u, y):
            if u not in tot: return 0
            return tot[u] - sub[u].get(realdir(u, y), 0)
        r = run(nodes, vpar, ew, lambda x: x in sinks, lambda x: f * inv[deg[x] - 1] % MOD, emit)
        H = {}
        for b, lst in r.items():
            h = {}
            for nb, ms in lst:
                if ms:
                    d = realdir(b, nb); h[d] = (h.get(d, 0) + ms) % MOD
            if h: H[b] = h
    print(ans % MOD)
main()
