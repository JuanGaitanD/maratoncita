// Factible(P) es monotono (quitar la 1a vuelta abarata todo). Para P fijo, desde el ultimo
// color hacia atras cada color toma el maximo ancho <= ancho del siguiente que le alcance.
#include <bits/stdc++.h>
using namespace std;
int n, k; vector<long long> pre, s;
bool ok(int P) {
    int R = P, W = P;
    for (int c = k - 1; c >= 0; c--) {
        if (R == 0) return true;
        int b = lower_bound(pre.begin(), pre.begin() + R + 1, pre[R] - s[c]) - pre.begin();
        b = max(b, R - W);
        W = R - b; R = b;
        if (W == 0) return false;
    }
    return R == 0;
}
int main() {
    scanf("%d %d", &n, &k); pre.assign(n + 1, 0); s.resize(k);
    for (int i = 0; i < n; i++) { long long x; scanf("%lld", &x); pre[i + 1] = pre[i] + x; }
    for (auto &x : s) scanf("%lld", &x);
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi + 1) / 2; if (ok(mid)) lo = mid; else hi = mid - 1; }
    printf("%d\n", lo);
}
