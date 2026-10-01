// Celdas peligrosas: a distancia Chebyshev <= H de una S/B (prefijos 2D). Refugios validos: R/Y/A no peligrosos;
// BFS multi-fuente (4 dir) da la distancia a un refugio. BFS final de Y a A por mar seguro con distancia <= D.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, H, D; cin >> n >> m >> H >> D;
    vector<string> g(n);
    for (auto &s : g) cin >> s;
    vector<vector<int>> pre(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)
        pre[i+1][j+1] = pre[i][j+1] + pre[i+1][j] - pre[i][j] + (g[i][j] == 'S' || g[i][j] == 'B');
    vector<vector<char>> danger(n, vector<char>(m, 0));
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
        int a = max(0, i - H), b = min(n, i + H + 1), c = max(0, j - H), d = min(m, j + H + 1);
        danger[i][j] = pre[b][d] - pre[a][d] - pre[b][c] + pre[a][c] > 0;
    }
    const int INF = 1 << 30;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    vector<vector<int>> dist(n, vector<int>(m, INF)), steps(n, vector<int>(m, -1));
    queue<pair<int,int>> q;
    int sy = 0, sx = 0;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
        char ch = g[i][j];
        if ((ch == 'R' || ch == 'Y' || ch == 'A') && !danger[i][j]) { dist[i][j] = 0; q.push({i, j}); }
        if (ch == 'Y') { sy = i; sx = j; }
    }
    while (!q.empty()) {
        auto p = q.front(); q.pop();
        for (int k = 0; k < 4; k++) {
            int x = p.first + dx[k], y = p.second + dy[k];
            if (x >= 0 && y >= 0 && x < n && y < m && dist[x][y] == INF) { dist[x][y] = dist[p.first][p.second] + 1; q.push({x, y}); }
        }
    }
    steps[sy][sx] = 0; q.push({sy, sx});
    while (!q.empty()) {
        auto p = q.front(); q.pop();
        if (g[p.first][p.second] == 'A') { cout << steps[p.first][p.second] << "\n"; return 0; }
        for (int k = 0; k < 4; k++) {
            int x = p.first + dx[k], y = p.second + dy[k];
            if (x < 0 || y < 0 || x >= n || y >= m || steps[x][y] >= 0 || danger[x][y] || dist[x][y] > D) continue;
            char ch = g[x][y];
            if (ch != '.' && ch != 'Y' && ch != 'A') continue;
            steps[x][y] = steps[p.first][p.second] + 1; q.push({x, y});
        }
    }
    cout << "OSIDEO WILL DIE\n";
}
