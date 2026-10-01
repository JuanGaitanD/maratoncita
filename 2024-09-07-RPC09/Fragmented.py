# Minimo de rectangulos = reflejos - (max cuerdas reflejo-reflejo sin cruzarse) + 1.
# Max cuerdas = H + V - emparejamiento maximo del grafo bipartito de cruces (Konig).
import sys
d = sys.stdin.buffer.read().split()
n = int(d[0]); P = [(int(d[1 + 2 * i]), int(d[2 + 2 * i])) for i in range(n)]
refl = set()
for i in range(n):
    a, b, c = P[i - 1], P[i], P[(i + 1) % n]
    if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) < 0: refl.add(i)
rpos = {P[i] for i in refl}
edges = [(P[i], P[(i + 1) % n]) for i in range(n)]
def chords(ax):  # ax=0: cuerdas horizontales (y fija), rayo en x
    o = 1 - ax; res = set()
    walls = [(e[0][ax], min(e[0][o], e[1][o]), max(e[0][o], e[1][o])) for e in edges if e[0][ax] == e[1][ax]]
    for i in refl:
        v = P[i]
        nb = P[i - 1] if P[i - 1][o] == v[o] else P[(i + 1) % n]  # vecino sobre la misma recta
        dr = 1 if nb[ax] < v[ax] else -1
        best = None
        for x, lo, hi in walls:
            if lo <= v[o] <= hi and (x - v[ax]) * dr > 0 and (best is None or abs(x - v[ax]) < abs(best - v[ax])):
                best = x
        q = [0, 0]; q[ax] = best; q[o] = v[o]; q = tuple(q)
        if q in rpos: res.add((v[o], min(v[ax], best), max(v[ax], best)))
    return list(res)
H = chords(0); V = chords(1)
adj = [[j for j, (x, y1, y2) in enumerate(V) if x1 <= x <= x2 and y1 <= y <= y2] for (y, x1, x2) in H]
match = [-1] * len(V)
def aug(u, seen):
    for v in adj[u]:
        if not seen[v]:
            seen[v] = True
            if match[v] < 0 or aug(match[v], seen): match[v] = u; return True
    return False
sys.setrecursionlimit(10000)
M = sum(aug(u, [False] * len(V)) for u in range(len(H)))
print(len(refl) - (len(H) + len(V) - M) + 1)
