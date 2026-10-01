// Las B/C forman m segmentos alternantes separados por las A (|m - a| <= 1).
// Segmentos: p con una B extra, q con una C extra, r balanceados (2 formas, >= 1 par).
// Formas = sum m!/(p!q!r!) * 2^r * C(T - r + m - 1, m - 1) * (2 si m == a), T = b - p pares.
#include <bits/stdc++.h>
using namespace std;
const long long M = 1000000007;
long long F[700], I[700];
long long pw(long long b, long long e) {
    long long r = 1; b %= M;
    for (; e; e >>= 1, b = b * b % M) if (e & 1) r = r * b % M;
    return r;
}
long long comb(int x, int y) { return (y < 0 || x < 0 || x < y) ? 0 : F[x] * I[y] % M * I[x - y] % M; }
int main() {
    int a, b, c; cin >> a >> b >> c;
    F[0] = 1;
    for (int i = 1; i < 700; i++) F[i] = F[i - 1] * i % M;
    for (int i = 0; i < 700; i++) I[i] = pw(F[i], M - 2);
    long long ans = 0;
    for (int m = max(1, a - 1); m <= a + 1; m++)
        for (int p = 0; p <= m; p++) {
            int q = p - (b - c), r = m - p - q, T = b - p;
            if (q < 0 || r < 0 || T < r) continue;
            long long w = F[m] * I[p] % M * I[q] % M * I[r] % M * pw(2, r) % M * comb(T - r + m - 1, m - 1) % M;
            ans = (ans + w * (m == a ? 2 : 1)) % M;
        }
    cout << ans << "\n";
}
