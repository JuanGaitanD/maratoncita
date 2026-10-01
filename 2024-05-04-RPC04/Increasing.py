# Recorrido lineal: longitud de la racha estrictamente creciente actual.
import sys
v = list(map(int, sys.stdin.read().split()))[1:]
best = cur = 1
for i in range(1, len(v)):
    cur = cur + 1 if v[i] > v[i - 1] else 1
    best = max(best, cur)
print(best)
