// DP de triangulacion en cadenas a->b (sentido del poligono): C = costo minimo, A1/A2 = costo minimo
// con el triangulo apoyado en a-b conteniendo al hermano 1/2. Luego se prueba cada triangulo central (i,j,k)
// asignando las dos regiones de los hermanos a dos de sus lados. Diagonales que tocan un hermano: prohibidas.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const double INF = 1e18;
int n;
ll X[505], Y[505];
ll cross(ll ax, ll ay, ll bx, ll by) { return ax * by - ay * bx; }
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &X[i], &Y[i]);
    ll bx[2], by[2];
    for (int t = 0; t < 2; t++) scanf("%lld %lld", &bx[t], &by[t]);
    vector<vector<double> > D(n, vector<double>(n)), C(n, vector<double>(n, INF));
    vector<vector<double> > A[2] = {C, C};
    vector<vector<int> > S[2] = {vector<vector<int> >(n, vector<int>(n)), vector<vector<int> >(n, vector<int>(n))};
    for (int a = 0; a < n; a++)
        for (int b = 0; b < n; b++) {
            if (a == b) continue;
            for (int t = 0; t < 2; t++) {
                ll c = cross(X[b] - X[a], Y[b] - Y[a], bx[t] - X[a], by[t] - Y[a]);
                S[t][a][b] = (c > 0) - (c < 0);
            }
            if ((a + 1) % n == b || (b + 1) % n == a) { D[a][b] = 0; continue; }
            bool bad = false;
            for (int t = 0; t < 2; t++)
                if (S[t][a][b] == 0 && min(X[a], X[b]) <= bx[t] && bx[t] <= max(X[a], X[b]) &&
                    min(Y[a], Y[b]) <= by[t] && by[t] <= max(Y[a], Y[b])) bad = true;
            D[a][b] = bad ? INF : hypot((double)(X[a] - X[b]), (double)(Y[a] - Y[b]));
        }
    for (int a = 0; a < n; a++) C[a][(a + 1) % n] = 0;
    for (int L = 2; L < n; L++)
        for (int a = 0; a < n; a++) {
            int b = (a + L) % n;
            for (int l = 1; l < L; l++) {
                int v = (a + l) % n;
                double base = C[a][v] + C[v][b] + D[a][v] + D[v][b];
                if (base >= INF) continue;
                C[a][b] = min(C[a][b], base);
                for (int t = 0; t < 2; t++) {
                    int s1 = S[t][a][v], s2 = S[t][v][b], s3 = S[t][b][a];
                    if (s1 != 0 && s1 == s2 && s2 == s3) A[t][a][b] = min(A[t][a][b], base);
                }
            }
        }
    double best = INF;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            if (D[i][j] >= INF) continue;
            for (int k = j + 1; k < n; k++) {
                if (D[j][k] >= INF || D[k][i] >= INF) continue;
                int r[3][2] = {{i, j}, {j, k}, {k, i}};
                double edges = D[i][j] + D[j][k] + D[k][i];
                for (int p = 0; p < 3; p++)
                    for (int q = 0; q < 3; q++) {
                        if (p == q) continue;
                        int z = 3 - p - q;
                        double v = edges + A[0][r[p][0]][r[p][1]] + A[1][r[q][0]][r[q][1]] + C[r[z][0]][r[z][1]];
                        best = min(best, v);
                    }
            }
        }
    if (best >= INF / 2) puts("-1");
    else printf("%.6f\n", best);
}
