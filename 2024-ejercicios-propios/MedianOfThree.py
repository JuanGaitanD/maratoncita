# Ordenar los tres numeros y tomar el del medio.
import sys
d = list(map(int, sys.stdin.read().split()))
print(" ".join(str(sorted(d[1 + 3 * k:4 + 3 * k])[1]) for k in range(d[0])))
