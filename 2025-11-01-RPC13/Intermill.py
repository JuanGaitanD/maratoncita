# Ordenar molinos por t. Con los k mas cercanos, T = (w + sum 2*t*p) / sum p.
# Es la respuesta si T <= 2*t del siguiente molino (o no hay mas). Aritmetica entera exacta.
import sys
data = sys.stdin.buffer.read().split()
n, w = int(data[0]), int(data[1])
mills = sorted((int(data[3 + 2 * i]), int(data[2 + 2 * i])) for i in range(n))
num, den = w, 0
for k, (t, p) in enumerate(mills):
    num += 2 * t * p
    den += p
    if k == n - 1 or num <= 2 * mills[k + 1][0] * den:
        print("%.9f" % (num / den))
        break
