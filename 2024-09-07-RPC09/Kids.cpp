// dist[j] = prob. de que nadie haya ganado y el progreso global sea j. Cada nino:
// acc(i) = acc(i-1)*a_i + dist[i]; gana con acc(k); nuevo dist[i] = acc(i)*(1-a_{i+1}).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, k; scanf("%d %d", &n, &k); vector<double> a(k), dist(k, 0.0), nd(k);
    for (auto &x : a) scanf("%lf", &x);
    dist[0] = 1; double best = 0;
    for (int it = 0; it < n; it++) {
        double acc = 0;
        for (int i = 0; i < k; i++) { acc += dist[i]; nd[i] = acc * (1 - a[i]); acc *= a[i]; }
        best = max(best, acc); swap(dist, nd);
    }
    printf("%.10f\n", best);
}
