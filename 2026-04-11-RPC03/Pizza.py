# Suma las porciones por tamano y divide hacia arriba entre la capacidad de cada caja.
import sys
d = sys.stdin.read().split()
cap = {'S': 6, 'M': 8, 'L': 12}
tot = {'S': 0, 'M': 0, 'L': 0}
for i in range(int(d[0])):
    tot[d[1 + 2 * i]] += int(d[2 + 2 * i])
print(sum((tot[s] + cap[s] - 1) // cap[s] for s in cap))
