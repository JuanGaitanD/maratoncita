// Las ciudades perdidas no tocan a las sobrevivientes, asi que el orden de ataque entre las
// sobrevivientes es el de la simulacion pura (heap por grado). Luego, en reversa con DSU,
// se cuenta cuantas ciudades atacadas seguian conectadas a NY en su momento; respuesta = eso + 1.
#include <bits/stdc++.h>
using namespace std;
vector<int> par;
int find(int x) { while (par[x] != x) x = par[x] = par[par[x]]; return x; }
int main() {
    int n, m; scanf("%d %d", &n, &m); vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); adj[u].push_back(v); adj[v].push_back(u); }
    vector<int> deg(n + 1), order; vector<char> gone(n + 1, 0);
    priority_queue<pair<int, int>> pq;
    for (int i = 2; i <= n; i++) { deg[i] = adj[i].size(); pq.push({deg[i], -i}); }
    while (!pq.empty()) {
        int d = pq.top().first, v = -pq.top().second; pq.pop();
        if (gone[v] || d != deg[v]) continue;
        gone[v] = 1; order.push_back(v);
        for (int w : adj[v]) if (!gone[w] && w != 1) { deg[w]--; pq.push({deg[w], -w}); }
    }
    par.resize(n + 1); iota(par.begin(), par.end(), 0);
    vector<char> in(n + 1, 0); in[1] = 1; long long days = 1;
    for (int i = (int)order.size() - 1; i >= 0; i--) {
        int v = order[i]; in[v] = 1;
        for (int w : adj[v]) if (in[w]) par[find(w)] = find(v);
        if (find(v) == find(1)) days++;
    }
    printf("%lld\n", days);
}
