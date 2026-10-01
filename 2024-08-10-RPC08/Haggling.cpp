// k = cadena mas larga (siguiente inicio >= fin+1). Respuesta = corte minimo de vertices
// que toque todas las cadenas de largo k: flujo maximo en el DAG por capas, con nodos
// "cadena" por capa (ordenados por inicio) para que las aristas sean O(n).
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> g; vector<int> to, cap;
void add(int u, int v, int c) {
    g[u].push_back(to.size()); to.push_back(v); cap.push_back(c);
    g[v].push_back(to.size()); to.push_back(u); cap.push_back(0);
}
int main() {
    int n; scanf("%d", &n);
    vector<pair<long long,long long>> iv(n);
    for (auto &p : iv) scanf("%lld %lld", &p.first, &p.second);
    sort(iv.begin(), iv.end());
    vector<int> L(n, 1), R(n, 1);
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++)
        if (iv[j].second + 1 <= iv[i].first) L[i] = max(L[i], L[j] + 1);
    for (int i = n - 1; i >= 0; i--) for (int j = 0; j < n; j++)
        if (iv[j].first >= iv[i].second + 1) R[i] = max(R[i], R[j] + 1);
    int k = *max_element(L.begin(), L.end());
    vector<vector<int>> layer(k + 2);
    for (int i = 0; i < n; i++) if (L[i] + R[i] - 1 == k) layer[L[i]].push_back(i);
    int V = 2 + 3 * n, INF = n + 1;  // 0=s, 1=t, 2+i entrada, 2+n+i salida, 2+2n+i cadena
    g.assign(V, {});
    for (int l = 1; l <= k; l++) {
        auto &lst = layer[l];
        for (size_t p = 0; p < lst.size(); p++) {
            int j = lst[p];
            add(2 + 2 * n + j, 2 + j, INF);
            if (p + 1 < lst.size()) add(2 + 2 * n + j, 2 + 2 * n + lst[p + 1], INF);
            add(2 + j, 2 + n + j, 1);
            if (l == 1) add(0, 2 + j, 1);
            if (l == k) add(2 + n + j, 1, 1);
        }
    }
    for (int l = 1; l < k; l++)
        for (int i : layer[l])
            for (int j : layer[l + 1])
                if (iv[j].first >= iv[i].second + 1) { add(2 + n + i, 2 + 2 * n + j, INF); break; }
    int flow = 0;
    while (true) {
        vector<int> par(V, -1); par[0] = -2; queue<int> q; q.push(0);
        while (!q.empty() && par[1] == -1) {
            int u = q.front(); q.pop();
            for (int e : g[u]) if (cap[e] && par[to[e]] == -1) { par[to[e]] = e; q.push(to[e]); }
        }
        if (par[1] == -1) break;
        for (int v = 1; v != 0; v = to[par[v] ^ 1]) { cap[par[v]]--; cap[par[v] ^ 1]++; }
        flow++;
    }
    printf("%d\n", flow);
}
