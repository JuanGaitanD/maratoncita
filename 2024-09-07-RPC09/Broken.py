# Cada pieza debe calzar exactamente sobre aristas consecutivas del borde. Token por par de
# aristas consecutivas = (|e1|^2, e1.e2, e1 x e2, |e2|^2) (invariante a rotar/trasladar).
# Arreglo de sufijos del borde duplicado; cada pieza (4 variantes: espejo/reversa) se busca
# por busqueda binaria y marca la longitud cubierta; al final se revisa que toda arista quede.
import sys
def toks(x, y, cyc):
    k = len(x); r = []
    for i in range(k if cyc else k - 2):
        b, c = (i + 1) % k, (i + 2) % k
        dx1, dy1, dx2, dy2 = x[b] - x[i], y[b] - y[i], x[c] - x[b], y[c] - y[b]
        r.append((dx1 * dx1 + dy1 * dy1, dx1 * dx2 + dy1 * dy2, dx1 * dy2 - dy1 * dx2, dx2 * dx2 + dy2 * dy2))
    return r
def suffix_array(T):
    L = len(T); rk = T[:]; k = 1
    while True:
        key = [(rk[i], rk[i + k] if i + k < L else -1) for i in range(L)]
        sa = sorted(range(L), key=key.__getitem__)
        new = [0] * L
        for j in range(1, L):
            new[sa[j]] = new[sa[j - 1]] + (key[sa[j]] != key[sa[j - 1]])
        rk = new
        if rk[sa[-1]] == L - 1: return sa
        k <<= 1
def main():
    d = sys.stdin.buffer.read().split(); p = 2
    n, m = int(d[0]), int(d[1])
    X = [int(v) for v in d[p:p + 2 * n:2]]; Y = [int(v) for v in d[p + 1:p + 2 * n:2]]; p += 2 * n
    pt = toks(X, Y, True); ids = {t: i for i, t in enumerate(sorted(set(pt)))}
    T = [ids[t] for t in pt] * 2; L = 2 * n
    SA = suffix_array(T)
    ups = []; single = set()
    for _ in range(m):
        k = int(d[p]); x = [int(v) for v in d[p + 1:p + 1 + 2 * k:2]]; y = [int(v) for v in d[p + 2:p + 2 + 2 * k:2]]
        p += 1 + 2 * k
        if k == 2: single.add((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2); continue
        for v in range(4):
            xx = [-q for q in x] if v & 1 else x; yy = y
            if v & 2: xx = xx[::-1]; yy = yy[::-1]
            pat = []
            for t in toks(xx, yy, False):
                if t not in ids: pat = None; break
                pat.append(ids[t])
            if pat is None: continue
            P = len(pat); lo, hi = 0, L
            while lo < hi:
                md = (lo + hi) // 2; s = SA[md]
                if T[s:s + P] < pat: lo = md + 1
                else: hi = md
            a = lo; hi = L
            while lo < hi:
                md = (lo + hi) // 2; s = SA[md]
                if T[s:s + P] <= pat: lo = md + 1
                else: hi = md
            if a < lo: ups.append((P, a, lo))
    ups.sort(reverse=True)
    best = [0] * L; nxt = list(range(L + 1))
    def f(x):
        r = x
        while nxt[r] != r: r = nxt[r]
        while nxt[x] != r: nxt[x], x = r, nxt[x]
        return r
    for P, a, b in ups:
        r = f(a)
        while r < b: best[r] = P; nxt[r] = r + 1; r = f(r)
    diff = [0] * (2 * n + 2)
    for r in range(L):
        s = SA[r]
        if s < n and best[r]: diff[s] += 1; diff[s + best[r] + 1] -= 1
    cov = [0] * (2 * n + 1); c = 0
    for i in range(2 * n + 1): c += diff[i]; cov[i] = c
    for i in range(n):
        j = (i + 1) % n
        if cov[i] + cov[i + n] == 0 and (X[j] - X[i]) ** 2 + (Y[j] - Y[i]) ** 2 not in single:
            print("NO"); return
    print("YES")
main()
