// BFS sobre celdas; desde cada celda se recorre cada direccion manteniendo la
// pendiente maxima vista: j es visible si su pendiente >= esa maxima.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int r, c; cin >> r >> c;
    vector<string> h(r);
    for (auto &s : h) cin >> s;
    vector<vector<int>> dist(r, vector<int>(c, -1));
    dist[0][0] = 0;
    queue<pair<int,int>> q; q.push({0, 0});
    int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
    while (!q.empty()) {
        int y = q.front().first, x = q.front().second; q.pop();
        for (int d = 0; d < 4; d++) {
            int bn = 0, bd = 0;  // pendiente maxima bn/bd (bd=0: ninguna)
            for (int yy = y + dy[d], xx = x + dx[d], t = 1; yy >= 0 && yy < r && xx >= 0 && xx < c; yy += dy[d], xx += dx[d], t++) {
                int n = h[yy][xx] - h[y][x];
                if (bd == 0 || n * bd >= bn * t) {
                    if (dist[yy][xx] < 0) { dist[yy][xx] = dist[y][x] + 1; q.push({yy, xx}); }
                    bn = n; bd = t;
                }
            }
        }
    }
    cout << dist[r - 1][c - 1] - 1 << "\n";
}
