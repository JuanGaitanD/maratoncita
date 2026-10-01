// Respuesta directa: k^2 mod (10^18 + 3), usando __int128 para no desbordar.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    const unsigned long long M = 1000000000000000003ULL;
    int q; cin >> q;
    while (q--) {
        unsigned long long k; cin >> k;
        unsigned __int128 r = (unsigned __int128)(k % M) * (k % M) % M;
        cout << (unsigned long long)r << "\n";
    }
}
