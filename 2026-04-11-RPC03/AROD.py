# Se cuenta por caja envolvente w x h (con (mx-w+1)(my-h+1) traslaciones). Toda caja tiene un
# vertice en una esquina: (i) dos esquinas opuestas: 4 rectos y el resto obtusos (salvo la
# diagonal); (ii-b) dos esquinas adyacentes + un punto en el lado opuesto; (ii-a) una esquina y
# dos puntos en los lados lejanos (criba sobre x'*w < y(h-y)). Agudos = total - el resto.
import sys
from math import gcd, isqrt
mx, my = map(int, sys.stdin.read().split())

def side_a(W, H):
    # suma sobre cajas de la esquina (0,0), B=(w,y), C=(x,h), angulo en B (obtuso, recto)
    V = (H // 2) * (H - H // 2) + 1
    c = [0] * (V + 1)
    for xp in range(1, W + 1):
        for w in range(xp + 1, min(W, V // xp) + 1):
            c[w * xp] += W - w + 1
    G = [0] * (V + 1)
    for v in range(1, V + 1): G[v] = G[v - 1] + c[v - 1]
    ob = ri = 0
    for h in range(2, H + 1):
        so = sr = 0
        for y in range(1, h):
            t = y * (h - y); so += G[t]; sr += c[t]
        ob += (H - h + 1) * so; ri += (H - h + 1) * sr
    return ob, ri

def side_b(w, h):  # x en (0,w) con x(w-x) > h^2 (obtuso) y = h^2 (recto)
    D = w * w - 4 * h * h
    if D <= 0: return 0, (1 if D == 0 else 0)
    t = isqrt(D - 1)
    ob = 2 * (t // 2) + 1 if w % 2 == 0 else 2 * ((t + 1) // 2)
    s = isqrt(D)
    return ob, (2 if s * s == D else 0)

N = (mx + 1) * (my + 1)
total = N * (N - 1) * (N - 2) // 6
deg = 0
for dx in range(mx + 1):
    for dy in range(my + 1):
        if dx or dy:
            deg += (2 if dx and dy else 1) * (mx - dx + 1) * (my - dy + 1) * (gcd(dx, dy) - 1)
ob = ri = 0
for w in range(1, mx + 1):
    for h in range(1, my + 1):
        pl = (mx - w + 1) * (my - h + 1)
        o1, r1 = side_b(w, h); o2, r2 = side_b(h, w)
        ob += pl * (2 * ((w + 1) * (h + 1) - 3 - gcd(w, h)) + 2 * (o1 + o2))
        ri += pl * (4 + 2 * (r1 + r2))
o1, r1 = side_a(mx, my); o2, r2 = side_a(my, mx)
ob += 4 * (o1 + o2); ri += 4 * (r1 + r2)
print("%d\n%d\n%d\n%d" % (total - ob - ri - deg, ri, ob, deg))
