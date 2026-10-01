// Cada punto x (coordenada l_i o r_i) debe atenderse por ultima vez en tiempo >= R(x)=max t que lo cubre.
// Basta con esas coordenadas; los pendientes forman un intervalo y se atiende un extremo:
// DP O(K^2) por longitud del intervalo pendiente. Punto virtual 0 = entrada.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 4000000000000000000LL;
int main() {
    int n; scanf("%d", &n);
    vector<array<ll, 3>> rg(n); vector<ll> xs;
    for (auto &r : rg) { scanf("%lld %lld %lld", &r[0], &r[1], &r[2]); xs.push_back(r[0]); xs.push_back(r[1]); }
    sort(rg.begin(), rg.end()); sort(xs.begin(), xs.end()); xs.erase(unique(xs.begin(), xs.end()), xs.end());
    vector<ll> x = {0}, t = {0};
    priority_queue<pair<ll, ll>> h; int k = 0;
    for (ll c : xs) {
        while (k < n && rg[k][0] <= c) { h.push({rg[k][2], rg[k][1]}); k++; }
        while (h.top().second < c) h.pop();
        x.push_back(c); t.push_back(h.top().first);
    }
    int K = x.size();
    // A[i]: pendiente [i..i+ln-1], en x[i-1]; B[i]: mismo pendiente, en x[i+ln]
    vector<ll> A(2, INF), B(2, INF), nA, nB; A[1] = 0;
    for (int ln = K - 2; ln >= 0; ln--) {
        int sz = K - ln + 1;
        nA.assign(sz, INF); nB.assign(sz, INF);
        for (int i = 1; i < sz; i++) {
            ll v = INF;
            if (i >= 2 && A[i - 1] < INF) v = min(v, A[i - 1] + x[i - 1] - x[i - 2]);
            if (i + ln < K && B[i - 1] < INF) v = min(v, B[i - 1] + x[i + ln] - x[i - 1]);
            if (v < INF) nA[i] = max(v, t[i - 1]);
        }
        for (int i = 0; i + 1 < sz; i++) {
            ll v = INF;
            if (i >= 1 && A[i] < INF) v = min(v, A[i] + x[i + ln] - x[i - 1]);
            if (i + ln + 1 < K && B[i] < INF) v = min(v, B[i] + x[i + ln + 1] - x[i + ln]);
            if (v < INF) nB[i] = max(v, t[i + ln]);
        }
        swap(A, nA); swap(B, nB);
    }
    ll ans = INF;
    for (ll v : A) ans = min(ans, v);
    for (ll v : B) ans = min(ans, v);
    printf("%lld\n", ans);
}
