// Cada pieza debe calzar exactamente sobre aristas consecutivas del borde. Token por par de
// aristas consecutivas = (|e1|^2, e1.e2, e1 x e2, |e2|^2) (invariante a rotar/trasladar).
// Arreglo de sufijos del borde duplicado; cada pieza (4 variantes: espejo/reversa) se busca
// por busqueda binaria y marca la longitud cubierta; al final se revisa que toda arista quede.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll; typedef array<ll, 4> tok;
int L; vector<int> T, SA;
vector<tok> toks(const vector<ll> &x, const vector<ll> &y, bool cyc) {
    int k = x.size(), e = cyc ? k : k - 1; vector<tok> r;
    for (int i = 0; i + (cyc ? 0 : 1) < e; i++) {
        int a = i, b = (i + 1) % k, c = (i + 2) % k;
        ll dx1 = x[b] - x[a], dy1 = y[b] - y[a], dx2 = x[c] - x[b], dy2 = y[c] - y[b];
        r.push_back({dx1 * dx1 + dy1 * dy1, dx1 * dx2 + dy1 * dy2, dx1 * dy2 - dy1 * dx2, dx2 * dx2 + dy2 * dy2});
    }
    return r;
}
void buildSA() {
    SA.resize(L); vector<int> rk(T), tmp(L), cnt;
    iota(SA.begin(), SA.end(), 0);
    sort(SA.begin(), SA.end(), [](int a, int b) { return T[a] < T[b]; });
    for (int k = 1;; k <<= 1) {
        auto key = [&](int i) { return i + k < L ? rk[i + k] + 1 : 0; };
        int M = max(L, *max_element(rk.begin(), rk.end()) + 1) + 1;
        cnt.assign(M, 0); for (int i = 0; i < L; i++) cnt[key(i)]++;
        for (int i = 1; i < M; i++) cnt[i] += cnt[i - 1];
        for (int i = L - 1; i >= 0; i--) tmp[--cnt[key(i)]] = i;
        cnt.assign(M, 0); for (int i = 0; i < L; i++) cnt[rk[i]]++;
        for (int i = 1; i < M; i++) cnt[i] += cnt[i - 1];
        for (int i = L - 1; i >= 0; i--) SA[--cnt[rk[tmp[i]]]] = tmp[i];
        tmp[SA[0]] = 0;
        for (int i = 1; i < L; i++)
            tmp[SA[i]] = tmp[SA[i - 1]] + (rk[SA[i]] != rk[SA[i - 1]] || key(SA[i]) != key(SA[i - 1]));
        rk = tmp; if (rk[SA[L - 1]] == L - 1) break;
    }
}
int cmpSuf(int s, const vector<int> &p) {  // <0 sufijo menor, 0 si p es prefijo, >0 mayor
    for (size_t j = 0; j < p.size(); j++) {
        if (s + (int)j >= L) return -1;
        if (T[s + j] != p[j]) return T[s + j] < p[j] ? -1 : 1;
    }
    return 0;
}
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<ll> X(n), Y(n); for (int i = 0; i < n; i++) scanf("%lld %lld", &X[i], &Y[i]);
    vector<tok> pt = toks(X, Y, true), uni = pt;
    sort(uni.begin(), uni.end()); uni.erase(unique(uni.begin(), uni.end()), uni.end());
    L = 2 * n; T.resize(L);
    for (int i = 0; i < n; i++) T[i] = T[i + n] = lower_bound(uni.begin(), uni.end(), pt[i]) - uni.begin();
    buildSA();
    vector<array<int, 3>> ups;  // (largo, lo, hi)
    set<ll> single;
    for (int i = 0; i < m; i++) {
        int k; scanf("%d", &k); vector<ll> x(k), y(k);
        for (int j = 0; j < k; j++) scanf("%lld %lld", &x[j], &y[j]);
        if (k == 2) { single.insert((x[1]-x[0])*(x[1]-x[0]) + (y[1]-y[0])*(y[1]-y[0])); continue; }
        for (int v = 0; v < 4; v++) {
            vector<ll> xx = x, yy = y;
            if (v & 1) for (auto &q : xx) q = -q;
            if (v & 2) { reverse(xx.begin(), xx.end()); reverse(yy.begin(), yy.end()); }
            vector<tok> t = toks(xx, yy, false); vector<int> p; bool ok = true;
            for (auto &q : t) {
                auto it = lower_bound(uni.begin(), uni.end(), q);
                if (it == uni.end() || *it != q) { ok = false; break; }
                p.push_back(it - uni.begin());
            }
            if (!ok) continue;
            int lo = 0, hi = L;
            while (lo < hi) { int md = (lo + hi) / 2; if (cmpSuf(SA[md], p) < 0) lo = md + 1; else hi = md; }
            int a = lo; hi = L;
            while (lo < hi) { int md = (lo + hi) / 2; if (cmpSuf(SA[md], p) <= 0) lo = md + 1; else hi = md; }
            if (a < lo) ups.push_back({(int)p.size(), a, lo});
        }
    }
    // pintar rangos de rangos por largo descendente (DSU "siguiente sin pintar")
    sort(ups.rbegin(), ups.rend());
    vector<int> best(L, 0), nxt(L + 1); iota(nxt.begin(), nxt.end(), 0);
    function<int(int)> f = [&](int x) { while (nxt[x] != x) x = nxt[x] = nxt[nxt[x]]; return x; };
    for (auto &u : ups) for (int r = f(u[1]); r < u[2]; r = f(r)) { best[r] = u[0]; nxt[r] = r + 1; }
    vector<int> diff(2 * n + 2, 0);
    for (int r = 0; r < L; r++) { int s = SA[r]; if (s < n && best[r]) { diff[s]++; diff[s + best[r] + 1]--; } }
    bool all = true; int c = 0; vector<int> cov(2 * n + 1);
    for (int i = 0; i <= 2 * n; i++) { c += diff[i]; cov[i] = c; }
    for (int i = 0; i < n; i++) {
        ll dx = X[(i + 1) % n] - X[i], dy = Y[(i + 1) % n] - Y[i];
        if (cov[i] + cov[i + n] == 0 && !single.count(dx * dx + dy * dy)) all = false;
    }
    puts(all ? "YES" : "NO");
}
