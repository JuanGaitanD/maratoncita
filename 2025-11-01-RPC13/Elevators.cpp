// Total = (viajes + trabajos, fijo) + esperas. Residuos c_i (instante ideal del tramo i, mod P=2e6) y
// fase k_j por ascensor: espera_i = (c_i + k_j - W) mod P. En el optimo cada ascensor tiene un tramo sin
// espera, asi que k_j = k_j' +- (c_{i-1}-c_i): se enumeran esos candidatos (arbol de profundidad <= 3)
// y para cada juego de fases se simula greedy (tomar el ascensor que pase primero), con poda.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll P = 2000000;
int n; vector<ll> c; ll best = LLONG_MAX;
void run(const ll* ks, int m) {
    ll W = 0;
    for (int i = 0; i < n; i++) {
        ll w = P;
        for (int j = 0; j < m; j++) w = min(w, ((c[i] + ks[j] - W) % P + P) % P);
        W += w;
        if (W >= best) return;
    }
    best = W;
}
int main() {
    scanf("%d", &n);
    vector<ll> F(n), T(n);
    for (auto& x : F) scanf("%lld", &x);
    for (auto& x : T) scanf("%lld", &x);
    ll A = 0, cur = 0;
    for (int i = 0; i < n; i++) {
        ll s = F[i] > cur ? cur : (P - cur) % P;
        c.push_back(((s - A) % P + P) % P); A += llabs(F[i] - cur) + T[i]; cur = F[i];
    }
    set<ll> Ds;
    for (int i = 1; i < n; i++) { ll x = ((c[i-1] - c[i]) % P + P) % P; Ds.insert(x); Ds.insert((P - x) % P); }
    vector<ll> D(Ds.begin(), Ds.end());
    ll ks[4]; ks[0] = (P - c[0]) % P; run(ks, 1);
    vector<ll> S1; for (ll x : D) S1.push_back((ks[0] + x) % P);
    sort(S1.begin(), S1.end()); S1.erase(unique(S1.begin(), S1.end()), S1.end());
    set<array<ll,3>> seen;
    for (size_t a = 0; a < S1.size(); a++) {
        ks[1] = S1[a]; run(ks, 2);
        set<ll> S2(S1.begin() + a + 1, S1.end());
        for (ll x : D) S2.insert((ks[1] + x) % P);
        S2.erase(ks[1]);
        for (ll k3 : S2) {
            ks[2] = k3; run(ks, 3);
            set<ll> S3 = S2; for (ll x : D) S3.insert((k3 + x) % P); S3.erase(k3);
            for (ll k4 : S3) {
                array<ll,3> key = {ks[1], k3, k4}; sort(key.begin(), key.end());
                if (!seen.insert(key).second) continue;
                ks[3] = k4; run(ks, 4);
            }
        }
    }
    printf("%lld\n", A + best);
}
