# DP: dp[i] = mejor minimo para los primeros i notas; el ultimo tramo j..i-1 es valido
# si la interseccion de rangos de octavas posibles no es vacia. O(n^2).
import sys
def main():
    d = list(map(int, sys.stdin.read().split()))
    n, l, h = d[0], d[1], d[2]
    a = d[3:3 + n]
    lo = [-((a[i] - l) // 12) for i in range(n)]   # ceil((l-a)/12)
    hi = [(h - a[i]) // 12 for i in range(n)]
    dp = [-1] * (n + 1)
    dp[0] = n + 1
    for i in range(1, n + 1):
        L, H, best = -10**9, 10**9, -1
        for j in range(i - 1, -1, -1):
            L = max(L, lo[j]); H = min(H, hi[j])
            if L > H:
                break
            if dp[j] >= 0:
                best = max(best, min(dp[j], i - j))
        dp[i] = best
    print(dp[n])
main()
