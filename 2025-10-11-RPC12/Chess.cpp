// Marca filas/columnas (R,Q), diagonales (Q) y casillas de caballo; luego cuenta. O(N^2 + M).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m; cin >> n >> m;
    vector<int> row(n + 1), col(n + 1), d1(2 * n + 2), d2(2 * n + 2);
    vector<vector<int>> kn(n + 1, vector<int>(n + 1));
    int dr[] = {1, 2, -1, -2, 1, 2, -1, -2}, dc[] = {2, 1, 2, 1, -2, -1, -2, -1};
    for (int k = 0; k < m; k++) {
        char p; int r, c; cin >> p >> r >> c;
        if (p == 'N') {
            kn[r][c] = 1;
            for (int i = 0; i < 8; i++) {
                int a = r + dr[i], b = c + dc[i];
                if (a >= 1 && a <= n && b >= 1 && b <= n) kn[a][b] = 1;
            }
        } else {
            row[r] = col[c] = 1;
            if (p == 'Q') d1[r - c + n] = d2[r + c] = 1;
        }
    }
    int cnt = 0;
    for (int r = 1; r <= n; r++)
        for (int c = 1; c <= n; c++)
            if (row[r] || col[c] || d1[r - c + n] || d2[r + c] || kn[r][c]) cnt++;
    cout << cnt << endl;
}
