# Regla de Smith: ordenar por m/c ascendente; cada switch paga c*(1+suma de m anteriores).
import sys
from functools import cmp_to_key
d = sys.stdin.buffer.read().split()
n = int(d[0]); sw = [(int(d[2 + 2 * i]), int(d[3 + 2 * i])) for i in range(n)]
sw.sort(key=cmp_to_key(lambda x, y: x[1] * y[0] - y[1] * x[0]))
pos = 1; tot = 0
for c, m in sw: tot += c * pos; pos += m
print(tot)
