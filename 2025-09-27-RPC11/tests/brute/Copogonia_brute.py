# Fuerza bruta: Floyd-Warshall para cada subconjunto. Genera Copogonia.9 (todas las vias necesarias).
import random, subprocess, sys, math, itertools
def solve(n, P, R, m):
    best = None
    for mask in range(1 << len(R)):
        d = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0; j = (i + 1) % n; w = math.dist(P[i], P[j]); d[i][j] = d[j][i] = min(d[i][j], w)
        c = 0
        for b, (u, v, cc) in enumerate(R):
            if mask >> b & 1:
                w = math.dist(P[u], P[v]); d[u][v] = d[v][u] = min(d[u][v], w); c += cc
        for q in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][q] + d[q][j] < d[i][j]: d[i][j] = d[i][q] + d[q][j]
        if max(map(max, d)) <= m + 1e-9 and (best is None or c < best): best = c
    return best, d
def poly(n):
    return [(round(5000 + 5000 * math.cos(2 * math.pi * i / n)), round(5000 + 5000 * math.sin(2 * math.pi * i / n))) for i in range(n)]
for it in range(60):
    n = random.randint(4, 9); P = poly(n)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n) if (v - u) % n not in (1, n - 1)]
    R = [(u, v, random.randint(1, 100)) for u, v in random.sample(pairs, min(len(pairs), random.randint(1, 5)))]
    _, dall = solve(n, P, [(u, v, 0) for u, v, _ in R], 1e18)
    lo = max(map(max, dall))
    per = sum(math.dist(P[i], P[(i + 1) % n]) for i in range(n))
    m = int(random.uniform(lo + 1, per / 2 - 1)) if per / 2 - 1 > lo + 1 else None
    if m is None: continue
    exp, _ = solve(n, P, R, m)
    inp = f"{n} {len(R)} {m}\n" + "".join(f"{x} {y}\n" for x, y in P) + "".join(f"{u+1} {v+1} {c}\n" for u, v, c in R)
    out = subprocess.run([sys.executable, "Copogonia.py"], input=inp, capture_output=True, text=True).stdout.strip()
    if int(out) != exp: print("BAD", inp, out, exp); break
else: print("ok")
