// DP por longitud t: estado (a = actos leidos del manuscrito 1, b = t - a del 2, manuscrito actual, cambios k).
// El ultimo registro queda determinado por (a, b, actual).
#include <bits/stdc++.h>
using namespace std;
int dp[2][152][2][152];
int main() {
    int K, T, n1, n2; cin >> K >> T >> n1;
    vector<string> A(n1); for (auto &s : A) cin >> s;
    cin >> n2;
    vector<string> B(n2); for (auto &s : B) cin >> s;
    const int NEG = -1000000;
    for (int a = 0; a <= T; a++) for (int c = 0; c < 2; c++) for (int k = 0; k <= K; k++) dp[1][a][c][k] = NEG;
    dp[1][1][0][0] = 0;
    for (int t = 1; t < T; t++) {
        int cu = t & 1, nx = cu ^ 1;
        for (int a = 0; a <= T; a++) for (int c = 0; c < 2; c++) for (int k = 0; k <= K; k++) dp[nx][a][c][k] = NEG;
        for (int a = 0; a <= t; a++) {
            int b = t - a;
            const string &nA = A[a % n1], &nB = B[b % n2];
            for (int c = 0; c < 2; c++) {
                if ((c == 0 && a == 0) || (c == 1 && b == 0)) continue;
                const string &last = c == 0 ? A[(a - 1) % n1] : B[(b - 1) % n2];
                for (int k = 0; k <= K; k++) {
                    int v = dp[cu][a][c][k];
                    if (v < 0) continue;
                    int k0 = k + (c != 0), k1 = k + (c != 1);
                    if (k0 <= K) dp[nx][a + 1][0][k0] = max(dp[nx][a + 1][0][k0], v + (last == nA));
                    if (k1 <= K) dp[nx][a][1][k1] = max(dp[nx][a][1][k1], v + (last == nB));
                }
            }
        }
    }
    int best = 0;
    for (int a = 0; a <= T; a++) for (int c = 0; c < 2; c++) for (int k = 0; k <= K; k++) best = max(best, dp[T & 1][a][c][k]);
    cout << best << "\n";
}
