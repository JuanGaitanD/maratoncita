// Abrir por completo las j cadenas mas cortas da P_j eslabones; quedan n-j piezas que
// necesitan n-j uniones. Respuesta = min_{0<=j<n} max(P_j, n-j).
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n; vector<long long> a(n); for (auto &x : a) cin >> x;
        sort(a.begin(), a.end());
        long long best = n, pre = 0;
        for (int j = 0; j < n; j++) { best = min(best, max(pre, (long long)n - j)); pre += a[j]; }
        cout << best << "\n";
    }
}
