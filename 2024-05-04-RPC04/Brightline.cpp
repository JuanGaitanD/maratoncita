// Camino minimo desde 1 con pesos negativos (sin ciclos negativos): SPFA (Bellman-Ford con cola).
// Se imprimen las ciudades con distancia minima < 0.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<vector<pair<int, long long>>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int s, e; char t; long long a; cin >> s >> e >> t >> a;
        g[s].push_back({e, t == 'r' ? -a : a});
    }
    const long long INF = LLONG_MAX / 4;
    vector<long long> dist(n + 1, INF);
    vector<bool> inq(n + 1, false);
    deque<int> q{1}; dist[1] = 0; inq[1] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop_front(); inq[u] = false;
        for (auto &p : g[u]) if (dist[u] + p.second < dist[p.first]) {
            dist[p.first] = dist[u] + p.second;
            if (!inq[p.first]) { inq[p.first] = true; q.push_back(p.first); }
        }
    }
    for (int v = 1; v <= n; v++) if (dist[v] < 0) cout << v << '\n';
}
