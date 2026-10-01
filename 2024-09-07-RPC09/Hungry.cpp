// Cambio de monedas (min monedas, ilimitadas) excluyendo un plato: divide y venceras sobre
// los platos (O(n w log n)); cada moneda se agrega con dp[x] = min(dp[x], dp[x-v]+1).
#include <bits/stdc++.h>
using namespace std;
int n, w; vector<int> c, ans; const int INF = 1e9;
void add(vector<int> &dp, int v) { for (int x = v; x <= w; x++) dp[x] = min(dp[x], dp[x - v] + 1); }
void solve(int l, int r, vector<int> dp) {
    if (l == r) { add(dp, 2 * c[l]); ans[l] = dp[w]; return; }
    int m = (l + r) / 2; vector<int> a = dp;
    for (int i = m + 1; i <= r; i++) add(a, c[i]);
    solve(l, m, a);
    for (int i = l; i <= m; i++) add(dp, c[i]);
    solve(m + 1, r, dp);
}
int main() {
    scanf("%d %d", &n, &w); c.resize(n); ans.resize(n);
    for (auto &x : c) scanf("%d", &x);
    vector<int> dp(w + 1, INF); dp[0] = 0;
    solve(0, n - 1, dp);
    for (int i = 0; i < n; i++) {
        if (i) printf(" ");
        if (ans[i] >= INF) printf("impossible"); else printf("%d", ans[i]);
    }
    printf("\n");
}
