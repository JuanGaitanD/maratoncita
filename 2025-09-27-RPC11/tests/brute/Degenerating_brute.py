# Fuerza bruta O(n^2): desde cada hub inicial se recorre el arbol acumulando la
# probabilidad de cada (nodo, nivel t). Sirve para validar Degenerating.py.
import sys
MOD = 998244353
def main():
    v = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k, p, q = v[:5]
    pos = {x: i for i, x in enumerate(v[5:5 + m])}
    val = v[5 + m:5 + m + n]
    adj = [[] for _ in range(n)]
    o = 5 + m + n
    for i in range(n - 1):
        a, b = v[o + 2 * i] - 1, v[o + 2 * i + 1] - 1
        adj[a].append(b); adj[b].append(a)
    al = p * pow(q, MOD - 2, MOD) % MOD
    apw = [al]
    for _ in range(m + 1): apw.append(apw[-1] * al % MOD)
    inv = [0] + [pow(i, MOD - 2, MOD) for i in range(1, n + 1)]
    ans = 0
    for s in range(n):
        st = [(s, -1, 0, 1)]
        while st:
            u, par, t, pr = st.pop()
            if pos.get(val[u], -1) == t: t += 1
            ch = len(adj[u]) - (par >= 0)
            if ch == 0:
                ans = (ans + pr * t) % MOD; continue
            f = apw[t]
            ans = (ans + pr * (1 - f) % MOD * t) % MOD
            nx = pr * f % MOD * inv[ch] % MOD
            for w in adj[u]:
                if w != par: st.append((w, u, t, nx))
    print(ans * pow(n, MOD - 2, MOD) % MOD)
main()
