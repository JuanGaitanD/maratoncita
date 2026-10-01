// Flood fill (DFS iterativo) desde '*' sobre celdas que no son '#'; se cuentan las celdas alcanzadas.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c;
    while (cin >> r >> c && r) {
        vector<string> g(r);
        for (auto &s : g) cin >> s;
        vector<pair<int,int>> st;
        for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (g[i][j] == '*') { st.push_back({i, j}); g[i][j] = '#'; }
        long long cnt = 1;
        int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
        while (!st.empty()) {
            auto q = st.back(); st.pop_back();
            for (int d = 0; d < 4; d++) {
                int x = q.first + dx[d], y = q.second + dy[d];
                if (x >= 0 && y >= 0 && x < r && y < c && g[x][y] != '#') { g[x][y] = '#'; cnt++; st.push_back({x, y}); }
            }
        }
        cout << cnt << "\n";
    }
}
