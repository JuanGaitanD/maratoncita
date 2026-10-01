# Abrir por completo las j cadenas mas cortas da P_j eslabones; quedan n-j piezas que
# necesitan n-j uniones. Respuesta = min_{0<=j<n} max(P_j, n-j).
import sys
d = sys.stdin.buffer.read().split(); p = 1; out = []
for _ in range(int(d[0])):
    n = int(d[p]); a = sorted(map(int, d[p + 1:p + 1 + n])); p += 1 + n
    best = n; pre = 0
    for j in range(n):
        best = min(best, max(pre, n - j)); pre += a[j]
    out.append(best)
print("\n".join(map(str, out)))
