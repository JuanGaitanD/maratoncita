// Como P[i] < i, se recorre de N a 2: tamanos (suma de dist = sum sz*(n-sz) por arista),
// altura h y diametro F(p) = max(F(hijos), h[p] + h[hijo] + 1).
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<int> par(n + 1), sz(n + 1, 1), h(n + 1, 0), F(n + 1, 0);
    for (int i = 2; i <= n; i++) cin >> par[i];
    long long tot = 0;
    for (int i = n; i > 1; i--) {
        int p = par[i];
        tot += (long long)sz[i] * (n - sz[i]);
        sz[p] += sz[i];
        int c = h[i] + 1;
        F[p] = max(F[p], max(F[i], h[p] + c));
        h[p] = max(h[p], c);
    }
    string out = to_string(tot) + "\n";
    for (int i = 1; i <= n; i++) { out += to_string(F[i]); out += (i == n ? '\n' : ' '); }
    cout << out;
}
