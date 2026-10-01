// k <= 10: se prueban subconjuntos por DFS. La matriz de distancias se actualiza en O(n^2)
// al agregar cada via (u, v, w): d[i][j] = min(d[i][j], d[i][u]+w+d[v][j], d[i][v]+w+d[u][j]).
// Se poda en cuanto todos los pares quedan <= m o el costo supera el mejor.
#include <bits/stdc++.h>
using namespace std;
typedef vector<vector<double>> Mat;
int n, k; double m; long long best = LLONG_MAX;
vector<double> X, Y; vector<int> U, V; vector<long long> Cst;
void dfs(int i, const Mat &d, long long cost) {
    if (cost >= best) return;
    double mx = 0;
    for (auto &r : d) for (double x : r) mx = max(mx, x);
    if (mx <= m + 1e-9) { best = cost; return; }
    if (i == k) return;
    int u = U[i], v = V[i];
    double w = hypot(X[u] - X[v], Y[u] - Y[v]);
    Mat e = d;
    for (int a = 0; a < n; a++) for (int b = 0; b < n; b++)
        e[a][b] = min(d[a][b], min(d[a][u] + w + d[v][b], d[a][v] + w + d[u][b]));
    dfs(i + 1, e, cost + Cst[i]);
    dfs(i + 1, d, cost);
}
int main() {
    cin >> n >> k >> m;
    X.resize(n); Y.resize(n); U.resize(k); V.resize(k); Cst.resize(k);
    for (int i = 0; i < n; i++) cin >> X[i] >> Y[i];
    for (int i = 0; i < k; i++) { cin >> U[i] >> V[i] >> Cst[i]; U[i]--; V[i]--; }
    vector<double> pre(n + 1, 0);
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + hypot(X[i] - X[(i + 1) % n], Y[i] - Y[(i + 1) % n]);
    Mat d(n, vector<double>(n));
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
        double a = fabs(pre[i] - pre[j]); d[i][j] = min(a, pre[n] - a);
    }
    dfs(0, d, 0);
    cout << best << "\n";
}
