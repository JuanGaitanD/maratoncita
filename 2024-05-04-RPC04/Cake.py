# Area doble total S (shoelace). Para cada diagonal (i, j) no adyacente, la pieza i..j tiene
# area doble P; diferencia = |S - 2P| / 2. O(n^3) con n <= 100 basta.
import sys
d = list(map(int, sys.stdin.read().split()))
n = d[0]; X = d[1::2]; Y = d[2::2]
def area(i, j):
    idx = list(range(i, j + 1))
    return abs(sum(X[idx[t]] * Y[idx[t - 1]] - X[idx[t - 1]] * Y[idx[t]] for t in range(len(idx))))
S = area(0, n - 1)
best = min(abs(S - 2 * area(i, j)) for i in range(n) for j in range(i + 2, n) if not (i == 0 and j == n - 1))
print("%d.%d" % (best // 2, 5 * (best % 2)))
