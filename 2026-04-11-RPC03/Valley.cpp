// Simulacion por eventos: cuencas entre maximos locales (acantilados = infinito). Cada lago
// recibe lluvia r*ancho mas el desborde de lagos llenos vecinos; al llegar a su borde mas bajo
// se llena (desborda) o se fusiona con el vecino lleno al mismo nivel.
#include <bits/stdc++.h>
using namespace std;
int p, m; vector<double> X, Y;
double vol(int a, int b, double h) {
    double s = 0;
    for (int i = a; i < b; i++) {
        double lo = min(Y[i], Y[i + 1]), hi = max(Y[i], Y[i + 1]), w = X[i + 1] - X[i];
        if (h <= lo) continue;
        if (h >= hi) s += w * (h - (Y[i] + Y[i + 1]) / 2);
        else s += w * (h - lo) * (h - lo) / (2 * (hi - lo));
    }
    return s;
}
struct Lake { int l, r; double v; bool full; };
int main() {
    double r; cin >> p >> r >> m; X.resize(p); Y.resize(p);
    for (int i = 0; i < p; i++) cin >> X[i] >> Y[i];
    vector<double> nx(m), nh(m), ans(m, -1);
    for (auto &x : nx) cin >> x;
    for (int k = 0; k < m; k++) for (int i = 0; i + 1 < p; i++)
        if (X[i] <= nx[k] && nx[k] <= X[i + 1]) { nh[k] = Y[i] + (Y[i + 1] - Y[i]) * (nx[k] - X[i]) / (X[i + 1] - X[i]); break; }
    const double INF = 1e300;
    vector<int> bnd = {0}; vector<double> bh = {INF};
    for (int i = 1; i + 1 < p; i++) if (Y[i] > Y[i - 1] && Y[i] > Y[i + 1]) { bnd.push_back(i); bh.push_back(Y[i]); }
    bnd.push_back(p - 1); bh.push_back(INF);
    vector<Lake> lakes;
    for (size_t j = 0; j + 1 < bnd.size(); j++) lakes.push_back({(int)j, (int)j + 1, 0, false});
    double t = 0;
    while (true) {
        int K = lakes.size();
        vector<double> spill(K), rate(K, 0); vector<int> side(K);
        for (int i = 0; i < K; i++) { spill[i] = min(bh[lakes[i].l], bh[lakes[i].r]); side[i] = bh[lakes[i].l] < bh[lakes[i].r] ? -1 : 1; }
        for (int i = 0; i < K; i++) { int j = i; while (lakes[j].full) j += side[j]; rate[j] += r * (X[bnd[lakes[i].r]] - X[bnd[lakes[i].l]]); }
        double best = INF; int who = -1;
        for (int i = 0; i < K; i++) if (!lakes[i].full && spill[i] < INF) {
            double dt = (vol(bnd[lakes[i].l], bnd[lakes[i].r], spill[i]) - lakes[i].v) / rate[i];
            if (dt < best) { best = dt; who = i; }
        }
        for (int i = 0; i < K; i++) if (!lakes[i].full) {
            double a = X[bnd[lakes[i].l]], b = X[bnd[lakes[i].r]];
            for (int k = 0; k < m; k++) if (ans[k] < 0 && a < nx[k] && nx[k] < b && nh[k] <= spill[i]) {
                double dt = (vol(bnd[lakes[i].l], bnd[lakes[i].r], nh[k]) - lakes[i].v) / rate[i];
                if (dt <= best) ans[k] = t + max(dt, 0.0);
            }
        }
        if (who < 0) break;
        t += best;
        for (int i = 0; i < K; i++) if (!lakes[i].full) lakes[i].v += rate[i] * best;
        lakes[who].v = vol(bnd[lakes[who].l], bnd[lakes[who].r], spill[who]); lakes[who].full = true;
        int j = who + side[who];
        if (lakes[j].full && spill[j] == spill[who]) {
            int a = min(who, j), b = max(who, j);
            Lake nl = {lakes[a].l, lakes[b].r, lakes[a].v + lakes[b].v, false};
            lakes.erase(lakes.begin() + a, lakes.begin() + b + 1);
            lakes.insert(lakes.begin() + a, nl);
        }
    }
    for (double x : ans) printf("%.8f\n", x);
}
