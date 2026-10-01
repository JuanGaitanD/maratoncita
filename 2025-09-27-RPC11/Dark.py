# A(psi) = area libre con angulo en [-theta, psi] = R^2/2*(psi+theta) - parte de cada circulo
# del lado "angulo < psi" de la recta por el origen (segmento circular). A es creciente:
# biseccion para cada objetivo j*Total/k.
import sys
from math import asin, acos, sin, sqrt, pi, radians, degrees
def main():
    v = list(map(int, sys.stdin.read().split()))
    n, k, R, th = v[0], v[1], v[2], radians(v[3])
    C = []
    full0 = 0.0
    for i in range(n):
        r, f, d = v[4 + 3 * i], radians(v[5 + 3 * i]), v[6 + 3 * i] / 2
        a = asin(d / r)
        C.append((f - a, f + a, r, f, d, pi * d * d))
    total = R * R * th - sum(c[5] for c in C)
    def area(psi):
        s = R * R / 2 * (psi + th)
        for lo, hi, r, f, d, ar in C:
            if psi >= hi: s -= ar
            elif psi > lo:
                t = r * sin(f - psi)
                t = max(-d, min(d, t))
                s -= d * d * acos(t / d) - t * sqrt(d * d - t * t)
        return s
    out = []
    lo = -th
    for j in range(1, k):
        goal = total * j / k
        a, b = lo, th
        for _ in range(55):
            m = (a + b) / 2
            if area(m) < goal: a = m
            else: b = m
        lo = a
        out.append("%.10f" % (degrees(a) + 0.0 if abs(degrees(a)) > 5e-11 else 0.0))
    print("\n".join(out))
main()
