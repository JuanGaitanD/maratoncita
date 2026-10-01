# BFS sobre celdas; desde cada celda se recorre cada direccion manteniendo la
# pendiente maxima vista: j es visible si su pendiente >= esa maxima.
import sys
from collections import deque
def main():
    d = sys.stdin.read().split()
    r, c = int(d[0]), int(d[1])
    h = [list(map(int, d[2 + i])) for i in range(r)]
    dist = [[-1] * c for _ in range(r)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        if y == r - 1 and x == c - 1:
            break
        nd = dist[y][x] + 1
        h0 = h[y][x]
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            bn, bd = 0, 0  # pendiente maxima bn/bd (bd=0: ninguna)
            yy, xx, t = y + dy, x + dx, 1
            while 0 <= yy < r and 0 <= xx < c:
                n = h[yy][xx] - h0
                if bd == 0 or n * bd >= bn * t:
                    if dist[yy][xx] < 0:
                        dist[yy][xx] = nd
                        q.append((yy, xx))
                    bn, bd = n, t
                yy += dy; xx += dx; t += 1
    print(dist[r - 1][c - 1] - 1)
main()
