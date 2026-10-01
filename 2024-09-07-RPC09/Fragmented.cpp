// Minimo de rectangulos = reflejos - (max cuerdas reflejo-reflejo sin cruzarse) + 1.
// Max cuerdas = H + V - emparejamiento maximo del grafo bipartito de cruces (Konig).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll; typedef array<ll, 2> pt;
int n; vector<pt> P; vector<int> refl; set<pt> rpos;
vector<array<ll, 3>> chords(int ax) {  // (coord fija, desde, hasta)
    int o = 1 - ax; set<array<ll, 3>> res; vector<array<ll, 3>> walls;
    for (int i = 0; i < n; i++) { pt a = P[i], b = P[(i + 1) % n];
        if (a[ax] == b[ax]) walls.push_back({a[ax], min(a[o], b[o]), max(a[o], b[o])}); }
    for (int i : refl) {
        pt v = P[i], nb = P[(i + n - 1) % n][o] == v[o] ? P[(i + n - 1) % n] : P[(i + 1) % n];
        int dr = nb[ax] < v[ax] ? 1 : -1; ll best = -1;
        for (auto &w : walls)
            if (w[1] <= v[o] && v[o] <= w[2] && (w[0] - v[ax]) * dr > 0 && (best < 0 || llabs(w[0] - v[ax]) < llabs(best - v[ax])))
                best = w[0];
        pt q; q[ax] = best; q[o] = v[o];
        if (rpos.count(q)) res.insert({v[o], min(v[ax], best), max(v[ax], best)});
    }
    return vector<array<ll, 3>>(res.begin(), res.end());
}
vector<vector<int>> adj; vector<int> mt; vector<char> seen;
bool aug(int u) {
    for (int v : adj[u]) if (!seen[v]) { seen[v] = 1; if (mt[v] < 0 || aug(mt[v])) { mt[v] = u; return true; } }
    return false;
}
int main() {
    scanf("%d", &n); P.resize(n);
    for (auto &p : P) scanf("%lld %lld", &p[0], &p[1]);
    for (int i = 0; i < n; i++) {
        pt a = P[(i + n - 1) % n], b = P[i], c = P[(i + 1) % n];
        if ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) < 0) { refl.push_back(i); rpos.insert(b); }
    }
    auto H = chords(0), V = chords(1);
    adj.assign(H.size(), {});
    for (size_t i = 0; i < H.size(); i++) for (size_t j = 0; j < V.size(); j++)
        if (H[i][1] <= V[j][0] && V[j][0] <= H[i][2] && V[j][1] <= H[i][0] && H[i][0] <= V[j][2]) adj[i].push_back(j);
    mt.assign(V.size(), -1); int M = 0;
    for (size_t u = 0; u < H.size(); u++) { seen.assign(V.size(), 0); M += aug(u); }
    printf("%d\n", (int)refl.size() - ((int)H.size() + (int)V.size() - M) + 1);
}
