// Probar cada ancho W >= palabra mas larga; alto por greedy saltando con busqueda binaria
// sobre prefijos. Se empieza en W=sqrt(S) y se poda con la cota alto >= (S+1)/(W+1) y cortando si ya no mejora.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> q(n + 1, 0); long long mx = 0; string w;
    for (int i = 0; i < n; i++) { cin >> w; q[i + 1] = q[i] + w.size() + 1; mx = max(mx, (long long)w.size()); }
    long long S = q[n] - 1, best = S + 1;
    long long W0 = max(mx, (long long)sqrt((double)S));  // primero cerca del optimo para podar mejor
    for (long long it = mx - 1; it < S; it++) {
        long long W = it < mx ? W0 : it;
        if (W + 1 >= best) break;
        if (W + (S + W + 1) / (W + 1) >= best) continue;
        long long lim = best - W, lines = 0; int i = 0;
        while (i < n && lines < lim) {
            i = upper_bound(q.begin() + i, q.end(), q[i] + W + 1) - q.begin() - 1;
            lines++;
        }
        if (i == n && W + lines < best) best = W + lines;
    }
    cout << best << "\n";
}
