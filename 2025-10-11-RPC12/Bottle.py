# Volumenes tras d dias (sin bajar de 0) y porcentaje de alcohol.
import sys
d, a, o, da, do = map(int, sys.stdin.read().split())
a = max(0, a - d * da); o = max(0, o - d * do)
print("%.10f" % (100.0 * a / (a + o)))
