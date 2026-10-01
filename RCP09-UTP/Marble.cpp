// BFS sobre pares de posiciones. dest[dir][celda] = donde se detiene una canica sola (-1 si cae). Si ambas
// terminan en la misma celda, la mas cercana queda ahi y la otra justo antes; si alguna cae, el estado se descarta.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m; cin >> n >> m;
    string g, s;
    for (int i = 0; i < n; i++) { cin >> s; g += s; }
    int r1, c1, r2, c2; cin >> r1 >> c1 >> r2 >> c2;
    int N = n * m, dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    vector<vector<int>> dest(4, vector<int>(N, -1));
    for (int k = 0; k < 4; k++) for (int v = 0; v < N; v++) {
        if (g[v] == '#' || g[v] == 'O') continue;
        int i = v / m, j = v % m;
        while (true) {
            int x = i + dr[k], y = j + dc[k];
            if (x < 0 || y < 0 || x >= n || y >= m || g[x * m + y] == 'O') { i = -1; break; }
            if (g[x * m + y] == '#') break;
            i = x; j = y;
        }
        if (i >= 0) dest[k][v] = i * m + j;
    }
    int a = (r1 - 1) * m + c1 - 1, b = (r2 - 1) * m + c2 - 1;
    if (g[a] == 'G' && g[b] == 'G') { cout << 0 << "\n"; return 0; }
    vector<int> dist(N * N, -1);
    queue<int> q; dist[a * N + b] = 0; q.push(a * N + b);
    while (!q.empty()) {
        int st = q.front(); q.pop();
        a = st / N; b = st % N;
        for (int k = 0; k < 4; k++) {
            int x = dest[k][a], y = dest[k][b], delta = dr[k] * m + dc[k];
            if (x < 0 || y < 0) continue;
            if (x == y) { if (abs(a - x) < abs(b - x)) y = x - delta; else x = y - delta; }
            int ns = x * N + y;
            if (dist[ns] >= 0) continue;
            dist[ns] = dist[st] + 1;
            if (g[x] == 'G' && g[y] == 'G') { cout << dist[ns] << "\n"; return 0; }
            q.push(ns);
        }
    }
    cout << -1 << "\n";
}
