// BFS multi-fuente desde los lobos da la distancia de cada celda. Luego se activan celdas
// de mayor a menor distancia uniendolas con DSU; la respuesta es la distancia con la que
// (1,1) y (r,c) quedan conectados (maximo cuello de botella).
#include <bits/stdc++.h>
using namespace std;
vector<int> par;
int find(int a) { while (par[a] != a) a = par[a] = par[par[a]]; return a; }
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c; cin >> r >> c;
    string g, s;
    for (int i = 0; i < r; i++) { cin >> s; g += s; }
    int N = r * c;
    vector<int> dist(N, -1), q;
    for (int i = 0; i < N; i++) if (g[i] == 'W') { dist[i] = 0; q.push_back(i); }
    for (size_t h = 0; h < q.size(); h++) {
        int u = q[h], y = u / c, x = u % c, d = dist[u] + 1;
        int nb[4] = {x > 0 ? u - 1 : -1, x < c - 1 ? u + 1 : -1, y > 0 ? u - c : -1, y < r - 1 ? u + c : -1};
        for (int v : nb) if (v >= 0 && dist[v] < 0) { dist[v] = d; q.push_back(v); }
    }
    par.resize(N); iota(par.begin(), par.end(), 0);
    vector<char> on(N, 0);
    for (int k = N - 1; k >= 0; k--) {
        int u = q[k], y = u / c, x = u % c;
        on[u] = 1;
        int nb[4] = {x > 0 ? u - 1 : -1, x < c - 1 ? u + 1 : -1, y > 0 ? u - c : -1, y < r - 1 ? u + c : -1};
        for (int v : nb) if (v >= 0 && on[v]) par[find(u)] = find(v);
        if (on[0] && on[N - 1] && find(0) == find(N - 1)) { cout << dist[u] << "\n"; return 0; }
    }
}
