# DP de probabilidad sobre (i, j, l) = plantas baratas, normales y caras ya compradas.
# Mientras el total sea < L se sigue comprando (eleccion uniforme entre las restantes);
# al llegar a >= L se para: exito si el total <= H.
import sys
def main():
    L, H, C, N, E, c, n, e = map(int, sys.stdin.read().split())
    ans = 0.0
    cur = {(0, 0, 0): 1.0}                      # estados por numero de plantas compradas
    for _ in range(c + n + e):
        nxt = {}
        for (i, j, l), pr in cur.items():
            rem = c + n + e - i - j - l
            for di, dj, dl, cnt in ((1, 0, 0, c - i), (0, 1, 0, n - j), (0, 0, 1, e - l)):
                if cnt == 0: continue
                q = pr * cnt / rem
                a, b, g = i + di, j + dj, l + dl
                s = a * C + b * N + g * E
                if s >= L:
                    if s <= H: ans += q
                else:
                    k = (a, b, g); nxt[k] = nxt.get(k, 0.0) + q
        cur = nxt
    print("%.9f" % ans)
main()
