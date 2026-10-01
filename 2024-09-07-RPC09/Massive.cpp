// Entre dos instantes en que ambos estan quietos, cada uno usa una sola compania (distintas).
// Dijkstra denso sobre pares (u,v): (u,v)->(u',v') cuesta max(DX[u][u'],DY[v][v']) o al reves.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll; const ll INF = 1LL << 60; int n;
vector<vector<ll>> rd(int cnt) {
    vector<vector<ll>> D(n, vector<ll>(n, INF));
    for (int i = 0; i < n; i++) D[i][i] = 0;
    for (int i = 0; i < cnt; i++) { int u, v; ll w; scanf("%d %d %lld", &u, &v, &w); D[u-1][v-1] = min(D[u-1][v-1], w); }
    for (int k = 0; k < n; k++) for (int i = 0; i < n; i++) for (int j = 0; j < n; j++)
        D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
    return D;
}
int main() {
    int x, y; scanf("%d %d %d", &n, &x, &y);
    auto DX = rd(x), DY = rd(y);
    vector<ll> dist(n * n, INF); vector<bool> done(n * n, false); dist[0] = 0;
    while (true) {
        int b = -1;
        for (int i = 0; i < n * n; i++) if (!done[i] && (b < 0 || dist[i] < dist[b])) b = i;
        if (b == n * n - 1 || dist[b] >= INF) break;
        done[b] = true; int u = b / n, v = b % n; ll T = dist[b];
        for (int a = 0; a < n; a++) for (int c = 0; c < n; c++) {
            ll w = min(max(DX[u][a], DY[v][c]), max(DY[u][a], DX[v][c]));
            if (w < INF && T + w < dist[a * n + c]) dist[a * n + c] = T + w;
        }
    }
    printf("%lld\n", dist[n * n - 1]);
}
