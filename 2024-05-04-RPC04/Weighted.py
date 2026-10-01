# Ventana deslizante: W(i+1) = W(i) - suma(ventana i) + k*a[i+k]. Ordenar por (W, i).
import sys
d = sys.stdin.buffer.read().split()
n, k = int(d[0]), int(d[1])
a = list(map(int, d[2:2 + n]))
w = sum((j + 1) * a[j] for j in range(k))
s = sum(a[:k])
res = [(w, 1)]
for i in range(n - k):
    w += k * a[i + k] - s
    s += a[i + k] - a[i]
    res.append((w, i + 2))
res.sort()
sys.stdout.write("\n".join("%d %d" % (i, w) for w, i in res) + "\n")
