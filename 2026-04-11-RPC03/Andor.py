# DP de abajo hacia arriba: costo minimo para que cada nodo valga T y para que valga F.
# AND: T = suma, F = minimo; OR: T = minimo, F = suma. Hoja: 0 si ya tiene ese valor, 1 si no.
import sys
d = sys.stdin.read().split()
n, t = int(d[0]), d[1]
levels, pos = [], 2
cnt = 1
for _ in range(n):
    row = d[pos:pos + cnt]; pos += cnt
    levels.append(row)
    cnt = sum(int(e) for e in row if e not in ('T', 'F'))
below = []  # costos (T, F) de los nodos del nivel siguiente, en orden
for lv in range(n - 1, -1, -1):
    is_and = (t == 'A') == (lv % 2 == 0)
    cur, k = [], 0
    for e in levels[lv]:
        if e == 'T': cur.append((0, 1))
        elif e == 'F': cur.append((1, 0))
        else:
            ch = below[k:k + int(e)]; k += int(e)
            st = sum(c[0] for c in ch); sf = sum(c[1] for c in ch)
            mt = min(c[0] for c in ch); mf = min(c[1] for c in ch)
            cur.append((st, mf) if is_and else (mt, sf))
    below = cur
print(max(below[0]))
