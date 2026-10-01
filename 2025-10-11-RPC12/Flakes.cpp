// Para cada '+', el tamano es el minimo de las 8 rachas del caracter correcto. O(n*m*(n+m)).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m; cin >> n >> m;
    vector<string> g(n);
    for (auto &s : g) cin >> s;
    int di[] = {-1, 1, 0, 0, -1, 1, -1, 1}, dj[] = {0, 0, -1, 1, -1, 1, 1, -1};
    const char *ch = "||--\\\\//";
    int best = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (g[i][j] != '+') continue;
            int size = INT_MAX;
            for (int d = 0; d < 8; d++) {
                int k = 0, x = i + di[d], y = j + dj[d];
                while (x >= 0 && x < n && y >= 0 && y < m && g[x][y] == ch[d]) { k++; x += di[d]; y += dj[d]; }
                size = min(size, k);
            }
            best = max(best, size);
        }
    cout << best << endl;
}
