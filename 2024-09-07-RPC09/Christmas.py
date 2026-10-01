# Cuerda 2r*sin(phi/2) <= l  <=>  phi <= 2*asin(l/2r); phi uniforme en [0,pi].
import math
r, l = map(int, input().split())
p = 0.0 if l >= 2 * r else 1 - 2 * math.asin(l / (2 * r)) / math.pi
print("%.10f" % p)
