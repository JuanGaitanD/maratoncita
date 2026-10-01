# Para cada '+', el tamano es el minimo de las 8 rachas del caracter correcto. O(n*m*(n+m)).
import sys
def main():
    t = sys.stdin.read().split()
    n, m = int(t[0]), int(t[1])
    g = t[2:2 + n]
    dirs = ((-1, 0, '|'), (1, 0, '|'), (0, -1, '-'), (0, 1, '-'),
            (-1, -1, '\\'), (1, 1, '\\'), (-1, 1, '/'), (1, -1, '/'))
    best = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] != '+':
                continue
            size = 10**9
            for di, dj, ch in dirs:
                k, x, y = 0, i + di, j + dj
                while 0 <= x < n and 0 <= y < m and g[x][y] == ch:
                    k += 1; x += di; y += dj
                size = min(size, k)
            best = max(best, size)
    print(best)
main()
