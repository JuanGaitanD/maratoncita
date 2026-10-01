// Ventana deslizante: W(i+1) = W(i) - suma(ventana i) + k*a[i+k]. Ordenar por (W, i).
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, k; cin >> n >> k; vector<long long> a(n);
    for (auto &x : a) cin >> x;
    long long w = 0, s = 0;
    for (int j = 0; j < k; j++) w += (j + 1) * a[j], s += a[j];
    vector<pair<long long, int>> r{{w, 1}};
    for (int i = 0; i + k < n; i++) { w += k * a[i + k] - s; s += a[i + k] - a[i]; r.push_back({w, i + 2}); }
    sort(r.begin(), r.end());
    for (auto &p : r) cout << p.second << ' ' << p.first << '\n';
}
