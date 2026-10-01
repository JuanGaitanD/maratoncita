# En cada columna x las alturas alcanzables forman un intervalo (de la paridad de x).
# Como los vertices son enteros, basta mirar techo/piso en x y x+1: se precalcula ceil(min techo) y floor(max piso).
import sys


def values(pts, w, is_ceil):
    INF = 10 ** 9
    best = [INF if is_ceil else -INF] * (w + 1)
    pick = min if is_ceil else max
    for k, (x, y) in enumerate(pts):
        best[x] = pick(best[x], y)
        if k + 1 < len(pts):
            xb, yb = pts[k + 1]
            for X in range(x + 1, xb):
                num, den = y * (xb - x) + (yb - y) * (X - x), xb - x
                best[X] = pick(best[X], -((-num) // den) if is_ceil else num // den)
    return best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, w = data[0], data[1], data[2]
    ce = [(data[4 + 2 * i], data[5 + 2 * i]) for i in range(n)]
    o = 4 + 2 * n
    fl = [(data[o + 2 * i], data[o + 1 + 2 * i]) for i in range(m)]
    C, Fv = values(ce, w, True), values(fl, w, False)
    lo = hi = 0
    for x in range(w):
        Uu, Ud = min(C[x] - 1, C[x + 1] - 2), min(C[x] - 1, C[x + 1])
        Lu, Ld = max(Fv[x] + 1, Fv[x + 1]), max(Fv[x] + 1, Fv[x + 1] + 2)
        nlo, nhi = None, None
        for L, U, d in ((Lu, Uu, 1), (Ld, Ud, -1)):
            a, b = max(lo, L), min(hi, U)
            a += (a - lo) % 2
            b -= (hi - b) % 2
            if a <= b:
                nlo = a + d if nlo is None else min(nlo, a + d)
                nhi = b + d if nhi is None else max(nhi, b + d)
        if nlo is None:
            print("impossible")
            return
        lo, hi = nlo, nhi
    print(lo, hi)


main()
