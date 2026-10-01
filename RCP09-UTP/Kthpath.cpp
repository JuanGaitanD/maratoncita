// K veces: Dijkstra de S a D, y se eliminan las aristas del camino encontrado. El K-esimo camino es la respuesta.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, K, S, D; cin >> n >> m >> K >> S >> D;
    vector<vector<array<int,3>>> adj(n + 1);
    for (int i = 0; i < m; i++) { int a, b, w; cin >> a >> b >> w; adj[a].push_back({b, w, i}); adj[b].push_back({a, w, i}); }
    vector<char> alive(m, 1);
    vector<ll> dist; vector<int> path;
    for (int it = 0; it < K; it++) {
        dist.assign(n + 1, LLONG_MAX);
        vector<int> pv(n + 1, 0), pe(n + 1, -1);
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
        dist[S] = 0; pq.push({0, S});
        while (!pq.empty()) {
            ll dv = pq.top().first; int v = pq.top().second; pq.pop();
            if (dv > dist[v]) continue;
            if (v == D) break;
            for (auto &e : adj[v]) if (alive[e[2]] && dv + e[1] < dist[e[0]]) {
                dist[e[0]] = dv + e[1]; pv[e[0]] = v; pe[e[0]] = e[2]; pq.push({dist[e[0]], e[0]});
            }
        }
        path.assign(1, D);
        for (int v = D; v != S; ) { alive[pe[v]] = 0; v = pv[v]; path.push_back(v); }
    }
    cout << dist[D] << "\n";
    for (int i = (int)path.size() - 1; i >= 0; i--) cout << path[i] << (i ? " - " : "\n");
}
