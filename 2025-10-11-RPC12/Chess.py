# Marca filas/columnas (R,Q), diagonales (Q) y casillas de caballo; luego cuenta. O(N^2 + M).
import sys
def main():
    t = sys.stdin.read().split()
    n, m = int(t[0]), int(t[1])
    row = [0] * (n + 1); col = [0] * (n + 1)
    d1 = [0] * (2 * n + 2); d2 = [0] * (2 * n + 2)
    kn = set()
    for k in range(m):
        p, r, c = t[2 + 3 * k], int(t[3 + 3 * k]), int(t[4 + 3 * k])
        if p == 'N':
            kn.add((r, c))
            for dr, dc in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)):
                kn.add((r + dr, c + dc))
        else:
            row[r] = col[c] = 1
            if p == 'Q':
                d1[r - c + n] = d2[r + c] = 1
    cnt = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if row[r] or col[c] or d1[r - c + n] or d2[r + c] or (r, c) in kn:
                cnt += 1
    print(cnt)
main()
