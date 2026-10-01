# El volumen hasta altura x es proporcional a rho(x)^3 - r^3 (cono extendido), con rho lineal en x:
# rho^3 = (r^3 + R^3) / 2  ->  x = h (rho - r) / (R - r); si r == R, x = h / 2.
import sys
def main():
    d = sys.stdin.buffer.read().split()
    out = []
    for i in range(int(d[0])):
        r, R, h = float(d[3*i+1]), float(d[3*i+2]), float(d[3*i+3])
        if R - r < 1e-12: x = h / 2
        else: x = h * (((r**3 + R**3) / 2) ** (1/3) - r) / (R - r)
        out.append("%.9f" % x)
    print("\n".join(out))
main()
