// Dijkstra sobre estados (calle dirigida actual, largo del tramo continuo acumulado).
// Un par continuo suma al tramo (debe quedar <= d); un par no continuo reinicia el tramo.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m, k, D, s, t; cin >> n >> m >> k >> D >> s >> t;
    vector<vector<int>> L(n + 1, vector<int>(n + 1, 0)), adj(n + 1);
    for (int i = 0; i < m; i++) { int a, b, l; cin >> a >> b >> l; L[a][b] = L[b][a] = l; adj[a].push_back(b); adj[b].push_back(a); }
    map<pair<int,int>, set<int>> cont;
    for (int i = 0; i < k; i++) { int a, b, c; cin >> a >> b >> c; cont[{a, b}].insert(c); }
    // estado codificado: (a*(n+1)+b)*(D+2)+c
    int S = (n + 1) * (n + 1) * (D + 2);
    vector<int> dist(S, INT_MAX); vector<char> expanded((n + 1) * (n + 1), 0);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    auto push = [&](int a, int b, int c, int dd) {
        int id = (a * (n + 1) + b) * (D + 2) + c;
        if (dd < dist[id]) { dist[id] = dd; pq.push({dd, id}); }
    };
    for (int x : adj[s]) push(s, x, min(L[s][x], D + 1), L[s][x]);
    while (!pq.empty()) {
        int du = pq.top().first, id = pq.top().second; pq.pop();
        if (du > dist[id]) continue;
        int c = id % (D + 2), e = id / (D + 2), a = e / (n + 1), b = e % (n + 1);
        if (b == t) { cout << du << endl; return 0; }
        auto it = cont.find({a, b});
        bool first = !expanded[e]; expanded[e] = 1;
        for (int x : adj[b]) {
            if (x == a) continue;
            int l = L[b][x];
            if (it != cont.end() && it->second.count(x)) { if (c + l <= D) push(b, x, c + l, du + l); }
            else if (first) push(b, x, min(l, D + 1), du + l);
        }
    }
    cout << "impossible" << endl;
}
