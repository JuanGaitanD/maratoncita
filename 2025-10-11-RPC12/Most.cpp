// Grafo serie-paralelo: se reducen vertices de grado 2 (serie) y aristas paralelas.
// Cada arista compuesta guarda (mejor camino u-v, mejor ciclo interno); paralelo: ciclo = P1+P2.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> PC;
const ll NEG = -(1LL << 62);
vector<map<int, PC>> adj;
ll best = NEG;
void add(int a, int b, ll P, ll C) {
    auto it = adj[a].find(b);
    if (it != adj[a].end()) {
        ll P2 = it->second.first, C2 = it->second.second;
        C = max(max(C, C2), P + P2); P = max(P, P2);
        best = max(best, C);
    }
    adj[a][b] = adj[b][a] = PC(P, C);
}
int main() {
    int V, E; scanf("%d %d", &V, &E);
    adj.resize(V + 1);
    for (int k = 0; k < E; k++) { int a, b; ll s; scanf("%d %d %lld", &a, &b, &s); add(a, b, s, NEG); }
    vector<int> st;
    for (int v = 1; v <= V; v++) if (adj[v].size() == 2) st.push_back(v);
    int alive = V;
    while (!st.empty() && alive > 2) {
        int w = st.back(); st.pop_back();
        if (adj[w].size() != 2) continue;
        auto i1 = adj[w].begin(), i2 = next(i1);
        int a = i1->first, b = i2->first; PC x = i1->second, y = i2->second;
        adj[w].clear(); adj[a].erase(w); adj[b].erase(w); alive--;
        add(a, b, x.first + y.first, max(x.second, y.second));
        if (adj[a].size() == 2) st.push_back(a);
        if (adj[b].size() == 2) st.push_back(b);
    }
    printf("%lld\n", best);
}
