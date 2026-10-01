// DP: dp[i] = mejor minimo para los primeros i notas; tramo j..i-1 valido si la
// interseccion de rangos de octavas no es vacia. O(n^2).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, l, h; cin >> n >> l >> h;
    vector<int> lo(n), hi(n), dp(n + 1, -1);
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        int x = l - a; lo[i] = x >= 0 ? (x + 11) / 12 : -((-x) / 12);
        int y = h - a; hi[i] = y >= 0 ? y / 12 : -((-y + 11) / 12);
    }
    dp[0] = n + 1;
    for (int i = 1; i <= n; i++) {
        int L = -1000000, H = 1000000;
        for (int j = i - 1; j >= 0; j--) {
            L = max(L, lo[j]); H = min(H, hi[j]);
            if (L > H) break;
            if (dp[j] >= 0) dp[i] = max(dp[i], min(dp[j], i - j));
        }
    }
    cout << dp[n] << endl;
}
