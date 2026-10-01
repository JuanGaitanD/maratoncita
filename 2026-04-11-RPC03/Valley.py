# Simulacion por eventos: el terreno se parte en cuencas entre maximos locales (acantilados =
# infinito). Cada lago recibe lluvia r*ancho mas el desborde de lagos llenos vecinos; cuando un
# lago llega a su borde mas bajo se llena (desborda) o se fusiona con el vecino al mismo nivel.
import sys
d = sys.stdin.read().split()
p, r, m = int(d[0]), float(d[1]), int(d[2])
X = [int(d[3 + 2 * i]) for i in range(p)]; Y = [int(d[4 + 2 * i]) for i in range(p)]
nests = [int(x) for x in d[3 + 2 * p:3 + 2 * p + m]]
INF = float('inf')

def height(x):
    for i in range(p - 1):
        if X[i] <= x <= X[i + 1]:
            return Y[i] + (Y[i + 1] - Y[i]) * (x - X[i]) / (X[i + 1] - X[i])

def vol(a, b, h):  # area de agua a nivel h entre los puntos a..b
    s = 0.0
    for i in range(a, b):
        x0, x1, y0, y1 = X[i], X[i + 1], Y[i], Y[i + 1]
        lo, hi = min(y0, y1), max(y0, y1)
        if h <= lo: continue
        if h >= hi: s += (x1 - x0) * (h - (y0 + y1) / 2)
        else: s += (x1 - x0) * (h - lo) ** 2 / (2 * (hi - lo))
    return s

bnd = [0] + [i for i in range(1, p - 1) if Y[i] > Y[i - 1] and Y[i] > Y[i + 1]] + [p - 1]
bh = [INF] + [Y[i] for i in bnd[1:-1]] + [INF]
# lago: [indice borde izq, indice borde der] en bnd, volumen, lleno?
lakes = [[j, j + 1, 0.0, False] for j in range(len(bnd) - 1)]
ans = [None] * m
nh = [height(x) for x in nests]
t = 0.0
while True:
    K = len(lakes)
    spill = [min(bh[L[0]], bh[L[1]]) for L in lakes]
    side = [(-1 if bh[L[0]] < bh[L[1]] else 1) for L in lakes]
    rate = [0.0] * K
    for i, L in enumerate(lakes):
        j = i
        while lakes[j][3]: j += side[j]
        rate[j] += r * (X[bnd[L[1]]] - X[bnd[L[0]]])
    best, who = INF, -1
    for i, L in enumerate(lakes):
        if not L[3] and spill[i] < INF:
            dt = (vol(bnd[L[0]], bnd[L[1]], spill[i]) - L[2]) / rate[i]
            if dt < best: best, who = dt, i
    for i, L in enumerate(lakes):
        if L[3]: continue
        a, b = X[bnd[L[0]]], X[bnd[L[1]]]
        for k in range(m):
            if ans[k] is None and a < nests[k] < b and nh[k] <= spill[i]:
                dt = (vol(bnd[L[0]], bnd[L[1]], nh[k]) - L[2]) / rate[i]
                if dt <= best: ans[k] = t + max(dt, 0.0)
    if who < 0: break
    t += best
    for i, L in enumerate(lakes):
        if not L[3]: L[2] += rate[i] * best
    L = lakes[who]; L[2] = vol(bnd[L[0]], bnd[L[1]], spill[who]); L[3] = True
    j = who + side[who]
    if lakes[j][3] and spill[j] == spill[who]:  # mismo borde: se fusionan
        a, b = min(who, j), max(who, j)
        lakes[a:b + 1] = [[lakes[a][0], lakes[b][1], lakes[a][2] + lakes[b][2], False]]
print("\n".join("%.8f" % x for x in ans))
