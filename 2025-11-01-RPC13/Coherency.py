# Rejilla de celdas de 211 mm (> 80+80+50.8): solo se comparan modelos en celdas vecinas.
# Arista si 400*dist^2 <= (10*(d1+d2)+1016)^2 (todo entero). DSU para conexidad y grado >= 2 si n >= 7.
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    X = list(map(int, data[1:3 * n + 1:3]))
    Y = list(map(int, data[2:3 * n + 1:3]))
    D = list(map(int, data[3:3 * n + 1:3]))
    S = 211
    cells = {}
    for i in range(n):
        cells.setdefault((X[i] // S, Y[i] // S), []).append(i)
    par = list(range(n))
    deg = [0] * n

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    comps = n
    for (cx, cy), lst in cells.items():
        for dx, dy in ((0, 0), (1, -1), (1, 0), (1, 1), (0, 1)):
            other = cells.get((cx + dx, cy + dy))
            if other is None:
                continue
            same = dx == 0 and dy == 0
            for k, i in enumerate(lst):
                xi, yi, di = X[i], Y[i], D[i]
                for j in (lst[k + 1:] if same else other):
                    ex, ey = X[j] - xi, Y[j] - yi
                    t = 10 * (di + D[j]) + 1016
                    if 400 * (ex * ex + ey * ey) <= t * t:
                        deg[i] += 1
                        deg[j] += 1
                        a, b = find(i), find(j)
                        if a != b:
                            par[a] = b
                            comps -= 1
    ok = comps == 1 and (n < 7 or min(deg) >= 2)
    print("yes" if ok else "no")


main()
