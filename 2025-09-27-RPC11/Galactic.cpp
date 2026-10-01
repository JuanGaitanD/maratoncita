// Dijkstra sobre residuos mod m = min(S): d[r] = menor posicion alcanzable = r (mod m); desde ahi
// todo r + t*m tambien lo es. Aristas: +s_i, y saltos de agujero x -> x+delta (delta <= K) con
// x = 0 mod p_j, x+delta = 0 mod p_k: el menor x >= d[r] sale por CRT. Respuesta max(d) - m.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll egcd(ll a, ll b, ll &x, ll &y) { if (!b) { x = 1; y = 0; return a; } ll g = egcd(b, a % b, y, x); y -= a / b * x; return g; }
ll inv(ll a, ll md) { ll x, y; egcd(a % md, md, x, y); return ((x % md) + md) % md; }
ll md(ll a, ll b) { return (a % b + b) % b; }
struct C { ll c2, g, Mg, iv, L; int dl; };
int main() {
    int S, P, K; cin >> S >> P >> K;
    vector<ll> s(S), p(P);
    for (auto &x : s) cin >> x;
    for (auto &x : p) cin >> x;
    ll m = *min_element(s.begin(), s.end());
    set<array<ll, 3>> seen; vector<C> pre;
    for (ll a : p) for (ll b : p) for (int dl = 1; dl <= K; dl++) {
        ll g = __gcd(a, b), r2 = md(-dl, b);       // x = 0 (mod a), x = r2 (mod b)
        if (r2 % g) continue;
        ll M2 = a / g * b, t = md((r2 / g) * inv(a / g, b / g), b / g), c2 = md(a * t, M2);
        if (!seen.insert({c2, M2, dl}).second) continue;
        ll g2 = __gcd(m, M2), Mg = M2 / g2;
        pre.push_back({c2, g2, Mg, Mg > 1 ? inv(m / g2, Mg) : 0, m * Mg, dl});
    }
    const ll INF = LLONG_MAX;
    vector<ll> d(m, INF); d[0] = 0;
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq;
    pq.push({0, 0});
    auto relax = [&](ll y) { if (y < d[y % m]) { d[y % m] = y; pq.push({y, y % m}); } };
    while (!pq.empty()) {
        ll du = pq.top().first, r = pq.top().second; pq.pop();
        if (du > d[r]) continue;
        for (ll st : s) relax(du + st);
        for (auto &c : pre) {
            ll diff = c.c2 - r;
            if (md(diff, c.g)) continue;
            ll x = r + m * md((diff / c.g) % c.Mg * c.iv, c.Mg);
            if (x < du) x += (du - x + c.L - 1) / c.L * c.L;
            relax(x + c.dl);
        }
    }
    ll mx = *max_element(d.begin(), d.end());
    cout << (mx == INF || mx - m <= 0 ? -1 : mx - m) << "\n";
}
