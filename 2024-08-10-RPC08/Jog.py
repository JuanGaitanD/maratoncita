# Ir a la celda de la ruta mas cercana (Manhattan d) y correr en contra de Jesse:
# se encuentra una fase nueva cada medio segundo. Esperado = d + (n-1)/4.
import sys
d = sys.stdin.buffer.read().split()
x, y, n = int(d[0]), int(d[1]), int(d[2])
m = min(abs(int(d[3 + 2 * i]) - x) + abs(int(d[4 + 2 * i]) - y) for i in range(n))
print("%.2f" % ((4 * m + n - 1) / 4))
