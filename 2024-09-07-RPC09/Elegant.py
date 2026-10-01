# Con t = h/w: madera = w*f(t), area = 1.5*w^2*t  =>  area = 1.5*t*n^2/f(t)^2. Ternaria en t.
import math
n = int(input())
def g(t):
    f = 2 + 2 * t + 2 * math.sqrt(1 + t * t) + 2 * math.sqrt(0.25 + t * t)
    return 1.5 * t * n * n / (f * f)
lo, hi = 0.0, 10.0
for _ in range(200):
    a = lo + (hi - lo) / 3; b = hi - (hi - lo) / 3
    if g(a) < g(b): lo = a
    else: hi = b
print("%.10f" % g(lo))
