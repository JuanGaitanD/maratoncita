# Backtracking: el punto libre de menor indice forma triangulo con otros dos libres.
# Areas dobles enteras; se poda si (max - min) ya no mejora. Respuesta = D/2 exacta.
import sys
d = list(map(int, sys.stdin.read().split()))
n = d[0]; N = 3 * n
X = d[1::2]; Y = d[2::2]
A = [[[abs((X[j] - X[i]) * (Y[k] - Y[i]) - (X[k] - X[i]) * (Y[j] - Y[i])) for k in range(N)]
      for j in range(N)] for i in range(N)]
best = 10 ** 18
def go(used, lo, hi):
    global best
    if hi - lo >= best:
        return
    if used == (1 << N) - 1:
        best = hi - lo
        return
    i = 0
    while used >> i & 1:
        i += 1
    free = [j for j in range(i + 1, N) if not used >> j & 1]
    Ai = A[i]
    for x in range(len(free)):
        j = free[x]; Aij = Ai[j]
        for k in free[x + 1:]:
            a = Aij[k]
            go(used | 1 << i | 1 << j | 1 << k, min(lo, a), max(hi, a))
go(0, 10 ** 18, -1)
print("%d.%d" % (best // 2, 5 * (best % 2)))
