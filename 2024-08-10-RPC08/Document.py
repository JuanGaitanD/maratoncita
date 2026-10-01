# Probar cada ancho W >= palabra mas larga; alto por greedy saltando con bisect
# sobre prefijos. Se empieza en W=sqrt(S) y se poda con la cota alto >= (S+1)/(W+1) y cortando si ya no mejora.
import sys
from bisect import bisect_right
def main():
    d = sys.stdin.buffer.read().split()
    n = int(d[0])
    q = [0] * (n + 1)  # q[j] = suma de (largo+1) de las primeras j palabras
    for i in range(n):
        q[i + 1] = q[i] + len(d[1 + i]) + 1
    S = q[n] - 1
    mx = max(len(w) for w in d[1:n + 1])
    best = S + 1  # W = S, una linea
    W0 = max(mx, int(S ** 0.5))  # se evalua primero cerca del optimo para podar mejor
    for W in [W0] + list(range(mx, S)):
        if W + 1 >= best: break
        if W + (S + W + 1) // (W + 1) < best:  # cota inferior
            lim = best - W
            i = lines = 0
            while i < n and lines < lim:
                i = bisect_right(q, q[i] + W + 1, i) - 1
                lines += 1
            if i == n and W + lines < best:
                best = W + lines
    print(best)
main()
