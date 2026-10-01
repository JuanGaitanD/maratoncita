// Se mantienen los extremos (a, b) del diametro. Al agregar una hoja x solo puede cambiar a (x, a) o (x, b):
// distancias con LCA por binary lifting (la hoja nueva extiende las tablas en O(log)). Diametro inicial: doble BFS.
#include <bits/stdc++.h>
using namespace std;
const int MAXV = 300001, LOG = 19;
int up[LOG][MAXV], dep[MAXV];
int dist(int x, int y) {
    int res = dep[x] + dep[y];
    if (dep[x] < dep[y]) swap(x, y);
    for (int k = 0, diff = dep[x] - dep[y]; diff; k++, diff >>= 1) if (diff & 1) x = up[k][x];
    if (x != y) {
        for (int k = LOG - 1; k >= 0; k--) if (up[k][x] != up[k][y]) { x = up[k][x]; y = up[k][y]; }
        x = up[0][x];
    }
    return res - 2 * dep[x];
}
void link(int x, int y) {
    dep[x] = dep[y] + 1; up[0][x] = y;
    for (int k = 1; k < LOG; k++) up[k][x] = up[k - 1][up[k - 1][x]];
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<vector<int>> adj(MAXV);
    int root = -1;
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
        if (root < 0) root = u;
    }
    for (int k = 0; k < LOG; k++) up[k][root] = root;
    vector<int> order = {root};
    vector<char> seen(MAXV, 0); seen[root] = 1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int u : adj[v]) if (!seen[u]) { seen[u] = 1; link(u, v); order.push_back(u); }
    }
    int a = root;
    for (int v : order) if (dep[v] > dep[a]) a = v;
    int b = a, diam = 0;
    for (int v : order) { int t = dist(a, v); if (t > diam) { diam = t; b = v; } }
    string out = to_string(diam) + "\n";
    int q; cin >> q;
    while (q--) {
        int x, y; cin >> x >> y;
        link(x, y);
        int da = dist(x, a), db = dist(x, b);
        if (da >= db && da > diam) { diam = da; b = x; }
        else if (db > diam) { diam = db; a = x; }
        out += to_string(diam) + "\n";
    }
    cout << out;
}
