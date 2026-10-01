# Cambio de monedas (min monedas, ilimitadas) excluyendo un plato: divide y venceras sobre
# los platos (O(n w log n)); agregar una moneda v: dp[x] = min(dp[x], dp[x-v]+1).
import sys
import sys
d = sys.stdin.read().split()
n, w = int(d[0]), int(d[1]); c = list(map(int, d[2:2 + n]))
INF = 10 ** 9
def add(dp, v):
    for x in range(v, w + 1):
        t = dp[x - v] + 1
        if t < dp[x]: dp[x] = t
ans = [0] * n
def solve(l, r, dp):
    if l == r:
        add(dp, 2 * c[l]); ans[l] = dp[w]; return
    m = (l + r) // 2
    a = dp[:]
    for i in range(m + 1, r + 1): add(a, c[i])
    solve(l, m, a)
    for i in range(l, m + 1): add(dp, c[i])
    solve(m + 1, r, dp)
dp0 = [INF] * (w + 1); dp0[0] = 0
solve(0, n - 1, dp0)
print(" ".join("impossible" if v >= INF else str(v) for v in ans))
