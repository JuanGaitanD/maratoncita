// Rejilla de celdas de 211 mm (> 80+80+50.8): solo se comparan modelos en celdas vecinas.
// Arista si 400*dist^2 <= (10*(d1+d2)+1016)^2 (todo entero). DSU para conexidad y grado >= 2 si n >= 7.
#include <bits/stdc++.h>
using namespace std;
vector<int> par;
int find(int a) { while (par[a] != a) a = par[a] = par[par[a]]; return a; }
int main() {
    int n;
    scanf("%d", &n);
    vector<long long> X(n), Y(n), D(n);
    map<pair<long long, long long>, vector<int> > cells;
    const long long S = 211;
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld", &X[i], &Y[i], &D[i]);
        cells[make_pair(X[i] / S, Y[i] / S)].push_back(i);
    }
    par.resize(n);
    for (int i = 0; i < n; i++) par[i] = i;
    vector<int> deg(n, 0);
    int comps = n;
    int ddx[5] = {0, 1, 1, 1, 0}, ddy[5] = {0, -1, 0, 1, 1};
    for (auto &it : cells) {
        const vector<int> &lst = it.second;
        for (int d = 0; d < 5; d++) {
            auto o = cells.find(make_pair(it.first.first + ddx[d], it.first.second + ddy[d]));
            if (o == cells.end()) continue;
            const vector<int> &other = o->second;
            for (size_t a = 0; a < lst.size(); a++) {
                int i = lst[a];
                for (size_t b = (d == 0 ? a + 1 : 0); b < other.size(); b++) {
                    int j = other[b];
                    long long ex = X[j] - X[i], ey = Y[j] - Y[i], t = 10 * (D[i] + D[j]) + 1016;
                    if (400 * (ex * ex + ey * ey) <= t * t) {
                        deg[i]++; deg[j]++;
                        int u = find(i), v = find(j);
                        if (u != v) { par[u] = v; comps--; }
                    }
                }
            }
        }
    }
    bool ok = comps == 1 && (n < 7 || *min_element(deg.begin(), deg.end()) >= 2);
    puts(ok ? "yes" : "no");
}
