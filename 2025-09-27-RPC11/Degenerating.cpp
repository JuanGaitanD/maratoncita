// Recolectar x_{L+1} en b (pos(b)=L) exige llegar a b con nivel L: la masa viene de nodos con
// pos L-1 por caminos sin otros nodos de pos L. Por cada nivel se arma el arbol virtual de
// A_{L-1} U A_L y se pasan mensajes (subida/bajada) con pesos alpha^{L+1}/(deg-1) por nodo
// intermedio; la masa que llega a b por cada direccion se guarda para el siguiente nivel.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;
ll pw(ll b, ll e) { ll r = 1; b %= MOD; if (b < 0) b += MOD; while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; } return r; }
int n, LOG;
vector<int> par, dep, tin, deg;
vector<vector<int>> adj, upt;
vector<ll> inv, Q, Qi;
int jump(int x, int d) { int k = dep[x] - d; for (int j = 0; k; j++, k >>= 1) if (k & 1) x = upt[j][x]; return x; }
int lca(int a, int b) {
    if (dep[a] < dep[b]) swap(a, b);
    a = jump(a, dep[b]);
    if (a == b) return a;
    for (int j = LOG - 1; j >= 0; j--) if (upt[j][a] != upt[j][b]) { a = upt[j][a]; b = upt[j][b]; }
    return par[a];
}
// datos por nodo del arbol actual (indexados por nodo real)
vector<ll> S, upm, downm, ew, tot;
vector<int> vpar;
vector<char> isSink;
map<int, vector<pair<int, ll>>> H;      // sink -> (direccion real o -1 = inicio, masa)
map<int, map<int, ll>> sub;              // fuente -> direccion -> masa emitida por esa entrada
int realdir(int u, int y) { return vpar[u] == y ? par[u] : jump(y, dep[u] + 1); }
int main() {
    ll m, k, p, q;
    cin >> n >> m >> k >> p >> q;
    map<ll, int> posof;
    for (int i = 0; i < m; i++) { ll x; cin >> x; posof[x] = i; }
    vector<int> pos(n);
    for (int i = 0; i < n; i++) { ll x; cin >> x; pos[i] = posof.count(x) ? posof[x] : -1; }
    if (n == 1) { cout << (pos[0] == 0 ? 1 : 0) << "\n"; return 0; }
    adj.assign(n, {});
    for (int i = 0; i < n - 1; i++) { int a, b; cin >> a >> b; a--; b--; adj[a].push_back(b); adj[b].push_back(a); }
    ll al = p % MOD * pw(q, MOD - 2) % MOD, inv_n = pw(n, MOD - 2);
    deg.resize(n); for (int i = 0; i < n; i++) deg[i] = adj[i].size();
    inv.assign(n + 1, 0); inv[1] = 1;
    for (int i = 2; i <= n; i++) inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD;
    par.assign(n, -1); dep.assign(n, 0); tin.assign(n, 0);
    vector<int> order; vector<char> seen(n, 0);
    vector<int> st = {0}; seen[0] = 1;
    while (!st.empty()) {
        int u = st.back(); st.pop_back(); tin[u] = order.size(); order.push_back(u);
        for (int w : adj[u]) if (!seen[w]) { seen[w] = 1; par[w] = u; dep[w] = dep[u] + 1; st.push_back(w); }
    }
    LOG = 1; while ((1 << LOG) <= n) LOG++;
    upt.assign(LOG, vector<int>(n));
    for (int i = 0; i < n; i++) upt[0][i] = par[i] < 0 ? 0 : par[i];
    for (int j = 1; j < LOG; j++) for (int i = 0; i < n; i++) upt[j][i] = upt[j - 1][upt[j - 1][i]];
    Q.assign(n, 1); Qi.assign(n, 1);
    for (size_t i = 1; i < order.size(); i++) { int u = order[i]; Q[u] = Q[par[u]] * inv[deg[u] - 1] % MOD; Qi[u] = Qi[par[u]] * (deg[u] - 1) % MOD; }
    map<int, vector<int>> groups;
    for (int x = 0; x < n; x++) if (pos[x] >= 0) groups[pos[x]].push_back(x);
    S.assign(n, 0); upm.assign(n, 0); downm.assign(n, 0); ew.assign(n, 1); tot.assign(n, 0);
    vpar.assign(n, -1); isSink.assign(n, 0);
    vector<char> isSrc(n, 0);
    ll f = al; int L = 0;
    vector<ll> e0(n, 0);
    // emision de u hacia el vecino virtual y
    auto emit = [&](int u, int y) -> ll {
        if (L == 0) return e0[u];
        if (!isSrc[u]) return 0;
        auto &mp = sub[u]; auto it = mp.find(realdir(u, y));
        return (tot[u] - (it == mp.end() ? 0 : it->second) + MOD) % MOD;
    };
    auto run = [&](const vector<int> &nodes) {
        for (int x : nodes) S[x] = 0;
        for (int i = (int)nodes.size() - 1; i >= 1; i--) {
            int x = nodes[i];
            ll val = emit(x, vpar[x]);
            if (!isSink[x]) val = (val + f * inv[deg[x] - 1] % MOD * S[x]) % MOD;
            upm[x] = val * ew[x] % MOD;
            S[vpar[x]] = (S[vpar[x]] + upm[x]) % MOD;
        }
        downm[nodes[0]] = 0;
        for (size_t i = 1; i < nodes.size(); i++) {
            int x = nodes[i], u = vpar[x];
            ll val = emit(u, x);
            if (!isSink[u]) val = (val + f * inv[deg[u] - 1] % MOD * ((S[u] - upm[x] + downm[u] + MOD) % MOD)) % MOD;
            downm[x] = val * ew[x] % MOD;
        }
        map<int, vector<pair<int, ll>>> res;
        for (size_t i = 0; i < nodes.size(); i++) {
            int x = nodes[i];
            if (isSink[x] && i > 0) res[x].push_back({vpar[x], downm[x]});
            if (i > 0 && isSink[vpar[x]]) res[vpar[x]].push_back({x, upm[x]});
            if (isSink[x] && !res.count(x)) res[x];
        }
        return res;
    };
    // nivel 0: arbol completo
    for (int x : groups[0]) isSink[x] = 1;
    for (int x = 0; x < n; x++) { vpar[x] = par[x]; if (!isSink[x]) e0[x] = inv_n * al % MOD * inv[deg[x]] % MOD; }
    auto r0 = run(order);
    for (auto &e : r0) {
        vector<pair<int, ll>> h = {{-1, inv_n}};
        for (auto &pr : e.second) h.push_back({pr.first, pr.second});
        H[e.first] = h;
    }
    for (int x : groups[0]) isSink[x] = 0;
    ll ans = 0;
    while (!H.empty()) {
        for (auto &e : H) for (auto &pr : e.second) ans = (ans + pr.second) % MOD;
        L++;
        if (!groups.count(L)) break;
        f = pw(al, L + 1);
        sub.clear();
        vector<int> pts;
        for (auto &e : H) {
            int b = e.first; isSrc[b] = 1; pts.push_back(b);
            ll t = 0; auto &mp = sub[b];
            for (auto &pr : e.second) {
                int c = pr.first < 0 ? deg[b] : deg[b] - 1;
                ll v = pr.second * f % MOD * inv[c] % MOD;
                mp[pr.first] = (mp[pr.first] + v) % MOD; t += v;
            }
            tot[b] = t % MOD;
        }
        for (int x : groups[L]) { isSink[x] = 1; pts.push_back(x); }
        sort(pts.begin(), pts.end(), [&](int a, int b) { return tin[a] < tin[b]; });
        pts.erase(unique(pts.begin(), pts.end()), pts.end());
        vector<int> nodes = pts;
        for (size_t i = 0; i + 1 < pts.size(); i++) nodes.push_back(lca(pts[i], pts[i + 1]));
        sort(nodes.begin(), nodes.end(), [&](int a, int b) { return tin[a] < tin[b]; });
        nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());
        vector<int> stk;
        for (int x : nodes) {
            while (!stk.empty() && lca(stk.back(), x) != stk.back()) stk.pop_back();
            vpar[x] = -1;
            if (!stk.empty()) {
                int u = stk.back(); vpar[x] = u;
                ew[x] = pw(f, dep[x] - dep[u] - 1) * Q[par[x]] % MOD * Qi[u] % MOD;
            }
            stk.push_back(x);
        }
        auto r = run(nodes);
        map<int, vector<pair<int, ll>>> NH;
        for (auto &e : r) {
            int b = e.first; map<int, ll> h;
            for (auto &pr : e.second) if (pr.second) { int d = realdir(b, pr.first); h[d] = (h[d] + pr.second) % MOD; }
            if (!h.empty()) NH[b] = vector<pair<int, ll>>(h.begin(), h.end());
        }
        for (auto &e : H) isSrc[e.first] = 0;
        for (int x : groups[L]) isSink[x] = 0;
        H.swap(NH);
    }
    cout << ans % MOD << "\n";
}
