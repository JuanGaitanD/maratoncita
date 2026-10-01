// En cada columna x las alturas alcanzables forman un intervalo (de la paridad de x).
// Como los vertices son enteros, basta mirar techo/piso en x y x+1: se precalcula ceil(min techo) y floor(max piso).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll fdiv(ll a, ll b) { return a >= 0 ? a / b : -((-a + b - 1) / b); }  // floor, b > 0
vector<ll> values(const vector<pair<ll, ll> > &p, int w, bool isCeil) {
    const ll INF = 1e9;
    vector<ll> best(w + 1, isCeil ? INF : -INF);
    for (size_t k = 0; k < p.size(); k++) {
        ll x = p[k].first, y = p[k].second;
        best[x] = isCeil ? min(best[x], y) : max(best[x], y);
        if (k + 1 < p.size()) {
            ll xb = p[k + 1].first, yb = p[k + 1].second;
            for (ll X = x + 1; X < xb; X++) {
                ll num = y * (xb - x) + (yb - y) * (X - x), den = xb - x;
                if (isCeil) best[X] = min(best[X], -fdiv(-num, den));
                else best[X] = max(best[X], fdiv(num, den));
            }
        }
    }
    return best;
}
int main() {
    int n, m, w, h;
    scanf("%d %d %d %d", &n, &m, &w, &h);
    vector<pair<ll, ll> > ce(n), fl(m);
    for (auto &q : ce) scanf("%lld %lld", &q.first, &q.second);
    for (auto &q : fl) scanf("%lld %lld", &q.first, &q.second);
    vector<ll> C = values(ce, w, true), F = values(fl, w, false);
    ll lo = 0, hi = 0;
    for (int x = 0; x < w; x++) {
        ll L[2] = {max(F[x] + 1, F[x + 1]), max(F[x] + 1, F[x + 1] + 2)};
        ll U[2] = {min(C[x] - 1, C[x + 1] - 2), min(C[x] - 1, C[x + 1])};
        ll d[2] = {1, -1};
        bool any = false;
        ll nlo = 0, nhi = 0;
        for (int t = 0; t < 2; t++) {
            ll a = max(lo, L[t]), b = min(hi, U[t]);
            if ((a - lo) & 1) a++;
            if ((hi - b) & 1) b--;
            if (a <= b) {
                if (!any) { nlo = a + d[t]; nhi = b + d[t]; any = true; }
                else { nlo = min(nlo, a + d[t]); nhi = max(nhi, b + d[t]); }
            }
        }
        if (!any) { puts("impossible"); return 0; }
        lo = nlo; hi = nhi;
    }
    printf("%lld %lld\n", lo, hi);
}
