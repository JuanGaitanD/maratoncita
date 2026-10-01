// Regla de Smith: ordenar por m/c ascendente; cada switch paga c*(1+suma de m anteriores).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; long long M; scanf("%d %lld", &n, &M);
    vector<pair<long long, long long>> s(n);
    for (auto &p : s) scanf("%lld %lld", &p.first, &p.second);
    sort(s.begin(), s.end(), [](const pair<long long,long long>& x, const pair<long long,long long>& y) {
        return x.second * y.first < y.second * x.first; });
    long long pos = 1, tot = 0;
    for (auto &p : s) { tot += p.first * pos; pos += p.second; }
    printf("%lld\n", tot);
}
