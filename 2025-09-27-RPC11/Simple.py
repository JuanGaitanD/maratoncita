# Casa = rectangulo w*t x h*t centrado en (x, y). Para un centro fijo, el t maximo es el
# minimo sobre los 4 lados de una funcion lineal -> concava; ternaria anidada en x e y.
import sys
v = list(map(int, sys.stdin.read().split()))
P = [(v[2 * i], v[2 * i + 1]) for i in range(4)]
w, h = v[8], v[9]
gx = sum(p[0] for p in P) / 4; gy = sum(p[1] for p in P) / 4
E = []                                      # semiplanos a*x + b*y <= c
for i in range(4):
    (x1, y1), (x2, y2) = P[i], P[(i + 1) % 4]
    a, b = y2 - y1, x1 - x2
    c = a * x1 + b * y1
    if a * gx + b * gy > c:
        a, b, c = -a, -b, -c
    E.append((a, b, c, (abs(a) * w + abs(b) * h) / 2))

def best_t(x, y):
    return min((c - a * x - b * y) / k for a, b, c, k in E)

def tern(lo, hi, g):
    for _ in range(100):
        m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
        if g(m1) < g(m2): lo = m1
        else: hi = m2
    return g((lo + hi) / 2)

xs = [p[0] for p in P]; ys = [p[1] for p in P]
t = tern(min(xs), max(xs), lambda x: tern(min(ys), max(ys), lambda y: best_t(x, y)))
t = max(t, 0.0)
print("%.9f" % (w * h * t * t))
