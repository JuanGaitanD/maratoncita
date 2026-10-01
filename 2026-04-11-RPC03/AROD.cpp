// Conteo por caja envolvente w x h (con (mx-w+1)(my-h+1) traslaciones); ver README.
// (i) dos esquinas opuestas, (ii-b) dos esquinas adyacentes, (ii-a) una sola esquina (criba).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll isq(ll x) { ll s = (ll)sqrtl((long double)x); while (s * s > x) s--; while ((s + 1) * (s + 1) <= x) s++; return s; }
void sideA(ll W, ll H, ll &ob, ll &ri) {
    ll V = (H / 2) * (H - H / 2) + 1;
    vector<ll> c(V + 1, 0), G(V + 1, 0);
    for (ll xp = 1; xp <= W; xp++) for (ll w = xp + 1; w <= min(W, V / xp); w++) c[w * xp] += W - w + 1;
    for (ll v = 1; v <= V; v++) G[v] = G[v - 1] + c[v - 1];
    ob = ri = 0;
    for (ll h = 2; h <= H; h++) {
        ll so = 0, sr = 0;
        for (ll y = 1; y < h; y++) { ll t = y * (h - y); so += G[t]; sr += c[t]; }
        ob += (H - h + 1) * so; ri += (H - h + 1) * sr;
    }
}
void sideB(ll w, ll h, ll &ob, ll &ri) {
    ll D = w * w - 4 * h * h;
    if (D <= 0) { ob = 0; ri = D == 0; return; }
    ll t = isq(D - 1);
    ob = w % 2 == 0 ? 2 * (t / 2) + 1 : 2 * ((t + 1) / 2);
    ll s = isq(D); ri = s * s == D ? 2 : 0;
}
int main() {
    ll mx, my; cin >> mx >> my;
    ll N = (mx + 1) * (my + 1), total = N * (N - 1) / 2 * (N - 2) / 3, deg = 0, ob = 0, ri = 0;
    for (ll dx = 0; dx <= mx; dx++) for (ll dy = 0; dy <= my; dy++) if (dx || dy)
        deg += (dx && dy ? 2 : 1) * (mx - dx + 1) * (my - dy + 1) * (__gcd(dx, dy) - 1);
    for (ll w = 1; w <= mx; w++) for (ll h = 1; h <= my; h++) {
        ll pl = (mx - w + 1) * (my - h + 1), o1, r1, o2, r2;
        sideB(w, h, o1, r1); sideB(h, w, o2, r2);
        ob += pl * (2 * ((w + 1) * (h + 1) - 3 - __gcd(w, h)) + 2 * (o1 + o2));
        ri += pl * (4 + 2 * (r1 + r2));
    }
    ll o1, r1, o2, r2; sideA(mx, my, o1, r1); sideA(my, mx, o2, r2);
    ob += 4 * (o1 + o2); ri += 4 * (r1 + r2);
    cout << total - ob - ri - deg << "\n" << ri << "\n" << ob << "\n" << deg << "\n";
}
