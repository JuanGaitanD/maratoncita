// N(k): rutas de longitud k (Fibonacci); E(k) = E(k-1) + E(k-2) + N(k) escalones totales.
#include <bits/stdc++.h>
using namespace std;
int main() {
    const long long M = 1000000007;
    int n, q; scanf("%d %d", &n, &q);
    vector<long long> N(n + 2, 1), E(n + 2, 0);
    E[1] = 1;
    for (int k = 2; k <= n; k++) { N[k] = (N[k - 1] + N[k - 2]) % M; E[k] = (E[k - 1] + E[k - 2] + N[k]) % M; }
    while (q--) { int s, t; scanf("%d %d", &s, &t); printf("%lld\n", E[t - s]); }
}
