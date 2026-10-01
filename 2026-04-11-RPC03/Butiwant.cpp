// Mejor caso: todos los votos de cada eliminado (el menor en cada ronda) pasan al segundo.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int c; cin >> c; vector<long long> v(c);
    for (auto &x : v) cin >> x;
    sort(v.begin(), v.end());
    long long total = accumulate(v.begin(), v.end(), 0LL), me = v[c - 2];
    if (2 * v[c - 1] > total || c == 2) { cout << "IMPOSSIBLE TO WIN" << endl; return 0; }
    for (int i = 0; i < c - 2; i++) {
        me += v[i];
        if (2 * me > total) { cout << i + 1 << endl; return 0; }
    }
    cout << "IMPOSSIBLE TO WIN" << endl;
}
