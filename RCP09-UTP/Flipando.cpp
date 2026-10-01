// Planificacion en bosque minimizando sum w*C: se toma el grupo con mayor w/p y se pega detras del grupo de su
// padre (costo extra P_padre * W_hijo). Heap con borrado perezoso + Union-Find. Raiz virtual 0 con p = w = 0.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct E { ll w, p; int v, ver; };
struct Cmp { bool operator()(const E &a, const E &b) const { return a.w * b.p < b.w * a.p; } };  // max w/p arriba
vector<int> dsu;
int find(int x) { while (dsu[x] != x) x = dsu[x] = dsu[dsu[x]]; return x; }
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<ll> P(n + 1, 0), W(n + 1, 0);
    vector<int> par(n + 1, 0), ver(n + 1, 0);
    for (int i = 1; i <= n; i++) cin >> P[i];
    for (int i = 1; i <= n; i++) cin >> W[i];
    int m; cin >> m;
    for (int i = 0; i < m; i++) { int a, b; cin >> a >> b; par[a] = b; }
    dsu.resize(n + 1); iota(dsu.begin(), dsu.end(), 0);
    ll cost = 0;
    vector<E> init;
    for (int i = 1; i <= n; i++) { cost += P[i] * W[i]; init.push_back({W[i], P[i], i, 0}); }
    priority_queue<E, vector<E>, Cmp> pq(Cmp(), move(init));
    while (!pq.empty()) {
        E e = pq.top(); pq.pop();
        int v = e.v;
        if (e.ver != ver[v]) continue;
        ver[v] = -1;
        int u = find(par[v]);
        dsu[v] = u;
        cost += P[u] * W[v];
        P[u] += P[v]; W[u] += W[v];
        if (u) { ver[u]++; pq.push({W[u], P[u], u, ver[u]}); }
    }
    cout << cost << "\n";
}
