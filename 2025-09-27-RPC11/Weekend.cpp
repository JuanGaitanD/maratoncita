// DP de probabilidad sobre (i, j, l) = plantas baratas, normales y caras ya compradas.
// Mientras el total sea < L se sigue comprando (eleccion uniforme entre las restantes);
// al llegar a >= L se para: exito si el total <= H.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
double dp[101][101][101];
int main() {
    ll L, H, C, N, E; int c, n, e;
    cin >> L >> H >> C >> N >> E >> c >> n >> e;
    double ans = 0;
    dp[0][0][0] = 1;
    // el orden lexicografico (i, j, l) respeta las transiciones (solo aumentan indices)
    for (int i = 0; i <= c; i++) for (int j = 0; j <= n; j++) for (int l = 0; l <= e; l++) {
        double pr = dp[i][j][l];
        if (pr == 0) continue;
        if (i * C + j * N + l * E >= L) continue;          // estado absorbente (ya contado)
        int rem = c + n + e - i - j - l;
        if (rem == 0) continue;
        int cnt[3] = {c - i, n - j, e - l};
        for (int t = 0; t < 3; t++) {
            if (!cnt[t]) continue;
            int a = i + (t == 0), b = j + (t == 1), g = l + (t == 2);
            double q = pr * cnt[t] / rem;
            ll s = a * C + b * N + g * E;
            if (s >= L) { if (s <= H) ans += q; }
            else dp[a][b][g] += q;
        }
    }
    printf("%.9f\n", ans);
}
