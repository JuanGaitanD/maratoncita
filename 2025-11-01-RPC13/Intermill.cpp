// Ordenar molinos por t. Con los k mas cercanos, T = (w + sum 2*t*p) / sum p.
// Es la respuesta si T <= 2*t del siguiente molino (o no hay mas). __int128 para no desbordar.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    long long w;
    scanf("%d %lld", &n, &w);
    vector<pair<long long, long long> > m(n);
    for (auto &x : m) scanf("%lld %lld", &x.second, &x.first);
    sort(m.begin(), m.end());
    __int128 num = w, den = 0;
    for (int k = 0; k < n; k++) {
        num += (__int128)2 * m[k].first * m[k].second;
        den += m[k].second;
        if (k == n - 1 || num <= (__int128)2 * m[k + 1].first * den) {
            printf("%.9f\n", (double)((long double)num / (long double)den));
            break;
        }
    }
}
