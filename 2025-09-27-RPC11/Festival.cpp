// a[n] = cadenas de largo n sin S, b[n] = cadenas cuya primera aparicion de S termina en n.
// K*a[n-1] = a[n] + b[n]  y  a[n-m] = sum_{j borde de S} b[n-m+j]  (Guibas-Odlyzko).
// Respuesta: K^N - a[N].  O(N * #bordes).
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
    long long N, K; string S;
    cin >> N >> K >> S;
    int m = S.size();
    vector<int> J;
    for (int j = 1; j < m; j++) if (S.compare(0, j, S, m - j, j) == 0) J.push_back(j);
    vector<long long> a(N + 1), b(N + 1, 0);
    a[0] = 1;
    long long pk = 1;
    for (int n = 1; n <= N; n++) {
        pk = pk * K % MOD;
        if (n < m) { a[n] = a[n - 1] * K % MOD; continue; }
        int o = n - m;
        long long x = a[o];
        for (int j : J) x -= b[o + j];
        x = (x % MOD + MOD) % MOD;
        b[n] = x;
        a[n] = ((a[n - 1] * K - x) % MOD + MOD) % MOD;
    }
    cout << ((pk - a[N]) % MOD + MOD) % MOD << "\n";
}
