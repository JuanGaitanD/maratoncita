# Genera los casos extra Nombre.9 (y .8 de tamano maximo) con salidas de fuerza bruta (o de formula cerrada).
# Uso: python gen.py   (desde cualquier carpeta)
import os, random, itertools, subprocess, sys
from collections import deque
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
R = random.Random(2026)
def save(name, k, inp, out):
    open(os.path.join(T, f"{name}.{k}.in"), "w", newline="\n").write(inp)
    open(os.path.join(T, f"{name}.{k}.out"), "w", newline="\n").write(out)

# A: simulacion directa del cifrado y comparar
words = ["".join(R.choice("abc") for _ in range(R.randint(1, 6))) for _ in range(30)]
K = 2; cnt = [0] * 26; c = 0; enc = []
for w in words:
    s = ""
    for ch in w:
        L = ord(ch) - 97; s += chr((L + c) % 26 + 97); cnt[L] += 1
        if cnt[L] % K == 0: c += 1
    enc.append(s)
save("Alejandro", 9, f"{len(words)} {K}\n{' '.join(enc)}\n", " ".join(words) + "\n")

# B: grilla aleatoria, BFS simple
def bet(g):
    r, cc = len(g), len(g[0])
    s = [(i, j) for i in range(r) for j in range(cc) if g[i][j] == "*"][0]
    seen = {s}; q = [s]
    for i, j in q:
        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= x < r and 0 <= y < cc and g[x][y] != "#" and (x, y) not in seen: seen.add((x, y)); q.append((x, y))
    return len(seen)
inp = ""; out = ""
for _ in range(5):
    r, cc = R.randint(2, 8), R.randint(2, 8)
    g = [[R.choice(".#") for _ in range(cc)] for _ in range(r)]
    g[R.randrange(r)][R.randrange(cc)] = "*"
    g = ["".join(x) for x in g]
    inp += f"{r} {cc}\n" + "\n".join(g) + "\n"; out += f"{bet(g)}\n"
save("Betito", 9, inp + "0 0\n", out)

# C: arbol aleatorio, distancias por BFS desde cada nodo
n = 12; P = [0, 0] + [R.randint(1, i - 1) for i in range(2, n + 1)]
adj = [[] for _ in range(n + 1)]
for i in range(2, n + 1): adj[i].append(P[i]); adj[P[i]].append(i)
def bfsd(s, ok):
    d = {s: 0}; q = [s]
    for v in q:
        for u in adj[v]:
            if u not in d and ok(u): d[u] = d[v] + 1; q.append(u)
    return d
def sub(x):
    S = {x}; ch = True
    while ch:
        ch = False
        for i in range(2, n + 1):
            if P[i] in S and i not in S: S.add(i); ch = True
    return S
tot = sum(sum(bfsd(u, lambda v: True).values()) for u in range(1, n + 1)) // 2
F = []
for x in range(1, n + 1):
    S = sub(x); F.append(max(max(bfsd(u, lambda v: v in S).values()) for u in S))
save("Company", 9, f"{n}\n{' '.join(map(str, P[2:]))}\n", f"{tot}\n{' '.join(map(str, F))}\n")

# E: fuerza bruta recursiva sobre todas las lecturas
def enar(K, T_, A, B):
    best = 0
    def rec(t, a, b, cur, k, last, e):
        nonlocal best
        if t == T_: best = max(best, e); return
        for nc in (0, 1):
            nk = k + (nc != cur)
            if nk > K: continue
            reg = A[a % len(A)] if nc == 0 else B[b % len(B)]
            rec(t + 1, a + (nc == 0), b + (nc == 1), nc, nk, reg, e + (reg == last))
    rec(1, 1, 0, 0, 0, A[0], 0)
    return best
A = [R.choice(["0", "1"]) for _ in range(5)]; B = [R.choice(["0", "1"]) for _ in range(4)]
save("Enarmonia", 9, f"3 12\n5\n" + "\n".join(A) + "\n4\n" + "\n".join(B) + "\n", f"{enar(3, 12, A, B)}\n")

# F: todas las permutaciones validas
n = 7; p = [R.randint(1, 5) for _ in range(n)]; w = [R.randint(1, 5) for _ in range(n)]
par = [0] + [R.randint(0, i - 1) for i in range(1, n)]  # 0 = sin restriccion para el nodo 1
cons = [(i + 1, par[i]) for i in range(1, n) if par[i] > 0]
best = None
for perm in itertools.permutations(range(1, n + 1)):
    pos = {v: i for i, v in enumerate(perm)}
    if any(pos[a] < pos[b] for a, b in cons): continue
    t = 0; c = 0
    for v in perm: t += p[v - 1]; c += t * w[v - 1]
    best = c if best is None else min(best, c)
save("Flipando", 9, f"{n}\n{' '.join(map(str, p))}\n{' '.join(map(str, w))}\n{len(cons)}\n" +
     "".join(f"{a} {b}\n" for a, b in cons), f"{best}\n")

# G: diametro recalculado con BFS tras cada insercion
labels = R.sample(range(0, 300000), 40)
n = 8; G = {labels[0]: []}; edges = []
for i in range(1, n):
    u = labels[i]; v = labels[R.randrange(i)]; G[u] = [v]; G[v].append(u); edges.append((u, v))
def diam():
    def far(s):
        d = {s: 0}; q = [s]
        for x in q:
            for y in G[x]:
                if y not in d: d[y] = d[x] + 1; q.append(y)
        b = max(d, key=d.get); return b, d[b]
    return far(far(labels[0])[0])[1]
outs = [diam()]; qs = []
for i in range(n, 40):
    x = labels[i]; y = labels[R.randrange(i)]; G[x] = [y]; G[y].append(x); qs.append((x, y)); outs.append(diam())
save("Guanex", 9, f"{n}\n" + "".join(f"{u} {v}\n" for u, v in edges) + f"{len(qs)}\n" + "".join(f"{x} {y}\n" for x, y in qs),
     "\n".join(map(str, outs)) + "\n")

# H: biseccion numerica del volumen
def hum(r, Rr, h):
    V = lambda x: x * (r * r + r * (r + (Rr - r) * x / h) + (r + (Rr - r) * x / h) ** 2)
    lo, hi = 0.0, h
    for _ in range(200):
        mid = (lo + hi) / 2
        if V(mid) * 2 < V(h): lo = mid
        else: hi = mid
    return lo
cs = [(round(R.uniform(1.5, 4.0), 2), round(R.uniform(4.0, 6.0), 2), round(R.uniform(7, 10), 2)) for _ in range(5)] + [(4.0, 6.0, 10.0), (1.5, 2.5, 7.0)]
save("Humbertov", 9, f"{len(cs)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in cs), "".join("%.9f\n" % hum(*x) for x in cs))

# I: maximo tamano (1e5 consultas con n cerca de 1e18) contra la formula exacta
M = 10 ** 9 + 7
ns = [10 ** 18 - R.randrange(10 ** 6) for _ in range(100000)] + [3, 1000000009, 1000000008, 1000000007]
save("Internal", 9, f"{len(ns)}\n" + "\n".join(map(str, ns)) + "\n", "\n".join(str(x * (x - 1) * (x - 2) // 6 % M) for x in ns) + "\n")

# J: componentes por BFS
inp = ""; out = ""
for _ in range(4):
    n = R.randint(1, 10); m = R.randint(0, 8) if n > 1 else 0
    E = [tuple(R.sample(range(1, n + 1), 2)) for _ in range(m)]
    adj = {i: [] for i in range(1, n + 1)}
    for a, b in E: adj[a].append(b); adj[b].append(a)
    seen = set(); sizes = []
    for s in range(1, n + 1):
        if s in seen: continue
        seen.add(s); q = [s]
        for v in q:
            for u in adj[v]:
                if u not in seen: seen.add(u); q.append(u)
        sizes.append(len(q))
    inp += f"{n} {m}\n" + "".join(f"{a} {b}\n" for a, b in E); out += f"{len(sizes)} {max(sizes)}\n"
save("Juan", 9, inp + "0 0\n", out)

# L: excentricidad de cada celda por BFS
def loc(g):
    H, W = len(g), len(g[0]); cells = [(i, j) for i in range(H) for j in range(W) if g[i][j] == "."]
    best = None
    for s in cells:
        d = {s: 0}; q = [s]
        for i, j in q:
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < H and 0 <= y < W and g[x][y] == "." and (x, y) not in d: d[(x, y)] = d[(i, j)] + 1; q.append((x, y))
        key = (max(d.values()), s[1], s[0])
        best = key if best is None else min(best, key)
    return best[2] + 1, best[1] + 1
def tree_grid(H, W):  # arbol aleatorio en grilla: crecer agregando celdas con un solo vecino pasillo
    g = [["#"] * W for _ in range(H)]; g[R.randrange(H)][R.randrange(W)] = "."
    for _ in range(H * W * 4):
        i, j = R.randrange(H), R.randrange(W)
        if g[i][j] == ".": continue
        nb = sum(1 for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if 0 <= x < H and 0 <= y < W and g[x][y] == ".")
        if nb == 1: g[i][j] = "."
    return ["".join(r) for r in g]
inp = "4\n"; out = ""
for c in range(1, 5):
    g = tree_grid(R.randint(3, 9), R.randint(3, 9))
    inp += f"{len(g)} {len(g[0])}\n" + "\n".join(g) + "\n"; out += "Case %d: %d %d\n" % ((c,) + loc(g))
save("Locate", 9, inp, out)
print("ok")
