# DP de triangulacion en cadenas a->b (sentido del poligono): C = costo minimo, A1/A2 = costo minimo
# con el triangulo apoyado en a-b conteniendo al hermano 1/2. Luego se prueba cada triangulo central (i,j,k)
# asignando las dos regiones de los hermanos a dos de sus lados. Diagonales que tocan un hermano: prohibidas.
import sys
from math import hypot


def sgn(c):
    return (c > 0) - (c < 0)


def main():
    d = list(map(int, sys.stdin.read().split()))
    n = d[0]
    X = d[1:2 * n + 1:2]
    Y = d[2:2 * n + 1:2]
    bx = [d[2 * n + 1], d[2 * n + 3]]
    by = [d[2 * n + 2], d[2 * n + 4]]
    INF = 1e18
    D = [[0.0] * n for _ in range(n)]
    S = [[[0] * n for _ in range(n)] for _ in range(2)]
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            bad = False
            for t in range(2):
                c = (X[b] - X[a]) * (by[t] - Y[a]) - (Y[b] - Y[a]) * (bx[t] - X[a])
                S[t][a][b] = sgn(c)
                if c == 0 and min(X[a], X[b]) <= bx[t] <= max(X[a], X[b]) and \
                        min(Y[a], Y[b]) <= by[t] <= max(Y[a], Y[b]):
                    bad = True
            if (a + 1) % n == b or (b + 1) % n == a:
                D[a][b] = 0.0
            else:
                D[a][b] = INF if bad else hypot(X[a] - X[b], Y[a] - Y[b])
    C = [[INF] * n for _ in range(n)]
    A = [[[INF] * n for _ in range(n)] for _ in range(2)]
    for a in range(n):
        C[a][(a + 1) % n] = 0.0
    for L in range(2, n):
        for a in range(n):
            b = (a + L) % n
            Ca = C[a]
            Da = D[a]
            best = INF
            b0 = INF
            b1 = INF
            for l in range(1, L):
                v = (a + l) % n
                base = Ca[v] + C[v][b] + Da[v] + D[v][b]
                if base >= INF:
                    continue
                if base < best:
                    best = base
                s3 = S[0][b][a]
                s1 = S[0][a][v]
                if s1 != 0 and s1 == S[0][v][b] and s1 == s3 and base < b0:
                    b0 = base
                s3 = S[1][b][a]
                s1 = S[1][a][v]
                if s1 != 0 and s1 == S[1][v][b] and s1 == s3 and base < b1:
                    b1 = base
            C[a][b] = best
            A[0][a][b] = b0
            A[1][a][b] = b1
    A0, A1 = A
    best = INF
    for i in range(n):
        for j in range(i + 1, n):
            if D[i][j] >= INF:
                continue
            for k in range(j + 1, n):
                if D[j][k] >= INF or D[k][i] >= INF:
                    continue
                r = ((i, j), (j, k), (k, i))
                e = D[i][j] + D[j][k] + D[k][i]
                for p in range(3):
                    ap = A0[r[p][0]][r[p][1]]
                    for q in range(3):
                        if p == q:
                            continue
                        z = 3 - p - q
                        v = e + ap + A1[r[q][0]][r[q][1]] + C[r[z][0]][r[z][1]]
                        if v < best:
                            best = v
    print(-1 if best >= INF / 2 else "%.6f" % best)


main()
