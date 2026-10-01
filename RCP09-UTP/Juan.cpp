// Union-Find con tamanos: razas = componentes, y la raza mas grande = mayor tamano.
#include <bits/stdc++.h>
using namespace std;
vector<int> par, sz;
int find(int x) { while (par[x] != x) x = par[x] = par[par[x]]; return x; }
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m;
    while (cin >> n >> m && (n || m)) {
        par.resize(n + 1); sz.assign(n + 1, 1);
        iota(par.begin(), par.end(), 0);
        int comp = n;
        for (int i = 0; i < m; i++) {
            int a, b; cin >> a >> b;
            a = find(a); b = find(b);
            if (a != b) { if (sz[a] < sz[b]) swap(a, b); par[b] = a; sz[a] += sz[b]; comp--; }
        }
        cout << comp << " " << *max_element(sz.begin() + 1, sz.end()) << "\n";
    }
}
