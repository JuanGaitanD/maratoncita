# Casos extra .9 para Dangerous, Kthpath y Marble con implementaciones de fuerza bruta independientes.
import os, random
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
R = random.Random(9)
def save(name, k, inp, out):
    open(os.path.join(T, f"{name}.{k}.in"), "w", newline="\n").write(inp)
    open(os.path.join(T, f"{name}.{k}.out"), "w", newline="\n").write(out)

# D: peligro y distancia a refugio calculados celda por celda (sin BFS multi-fuente)
def dang(n, m, H, D, g):
    cells = [(i, j) for i in range(n) for j in range(m)]
    bad = {(i, j) for i, j in cells if any(g[a][b] in "SB" and max(abs(a-i), abs(b-j)) <= H for a, b in cells)}
    refs = [(a, b) for a, b in cells if g[a][b] in "RYA" and (a, b) not in bad]
    ok = {(i, j) for i, j in cells if (i, j) not in bad and g[i][j] in ".YA" and any(abs(a-i)+abs(b-j) <= D for a, b in refs)}
    s = [c for c in cells if g[c[0]][c[1]] == "Y"][0]
    d = {s: 0}; q = [s]
    for i, j in q:
        if g[i][j] == "A": return str(d[(i, j)])
        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if (x, y) in ok and (x, y) not in d: d[(x, y)] = d[(i, j)] + 1; q.append((x, y))
    return "OSIDEO WILL DIE"
while True:
    n, m = 8, 10
    g = [[R.choice("........RS") for _ in range(m)] for _ in range(n)]
    g[0][0] = "Y"; g[n-1][m-1] = "A"
    for i, j in ((0, 1), (1, 0), (1, 1), (n-2, m-1), (n-1, m-2), (n-2, m-2)):
        if g[i][j] == "S": g[i][j] = "."
    g = ["".join(r) for r in g]
    res = dang(n, m, 1, 2, g)
    if res != "OSIDEO WILL DIE": break
save("Dangerous", 9, f"{n} {m}\n1 2\n" + "\n".join(g) + "\n", res + "\n")

# K: enumerar todos los caminos simples con las aristas aun disponibles
n = 7; E = []
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if R.random() < 0.6: E.append((a, b, R.randint(1, 10 ** 8)))
S, D, K = 1, 7, 2
alive = set(range(len(E)))
for _ in range(K):
    best = None
    def dfs(v, vis, cost, used):
        global best
        if v == D:
            if best is None or cost < best[0]: best = (cost, list(vis), list(used))
            return
        for i in alive:
            a, b, w = E[i]
            if v in (a, b):
                u = b if v == a else a
                if u not in vis: vis.append(u); used.append(i); dfs(u, vis, cost + w, used); vis.pop(); used.pop()
    dfs(S, [S], 0, [])
    alive -= set(best[2])
save("Kthpath", 9, f"{n} {len(E)} {K} {S} {D}\n" + "".join(f"{a} {b} {w}\n" for a, b, w in E),
     f"{best[0]}\n" + " - ".join(map(str, best[1])) + "\n")

# M: simulacion paso a paso (la canica de adelante se mueve primero)
def marble(n, m, g, s):
    def slide(p, o, dr, dc):
        i, j = p
        while True:
            x, y = i + dr, j + dc
            if not (0 <= x < n and 0 <= y < m) or g[x][y] == "O": return None
            if g[x][y] == "#" or (x, y) == o: return (i, j)
            i, j = x, y
    win = lambda st: all(g[a][b] == "G" for a, b in st)
    if win(s): return 0
    d = {s: 0}; q = [s]
    for st in q:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = st
            if (b[0]-a[0])*dr + (b[1]-a[1])*dc > 0:
                nb = slide(b, a, dr, dc); na = slide(a, nb, dr, dc) if nb else None
            else:
                na = slide(a, b, dr, dc); nb = slide(b, na, dr, dc) if na else None
            if na is None or nb is None: continue
            ns = (na, nb)
            if ns not in d:
                d[ns] = d[st] + 1
                if win(ns): return d[ns]
                q.append(ns)
    return -1
while True:
    n, m = 7, 7
    g = ["#" * m] + ["#" + "".join(R.choice("....#OG") for _ in range(m - 2)) + "#" for _ in range(n - 2)] + ["#" * m]
    free = [(i, j) for i in range(n) for j in range(m) if g[i][j] in ".G"]
    s = tuple(R.sample(free, 2))
    res = marble(n, m, g, s)
    if res > 1: break
save("Marble", 9, f"{n} {m}\n" + "\n".join(g) + f"\n{s[0][0]+1} {s[0][1]+1}\n{s[1][0]+1} {s[1][1]+1}\n", f"{res}\n")
print("ok")
