# Imprimir el menor de cada par.
import sys
d = list(map(int, sys.stdin.read().split()))
print(" ".join(str(min(d[1 + 2 * k], d[2 + 2 * k])) for k in range(d[0])))
