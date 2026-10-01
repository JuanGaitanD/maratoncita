// Suma las porciones por tamano y divide hacia arriba entre la capacidad de cada caja.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, l; char s; cin >> n;
    map<char, int> cap = {{'S', 6}, {'M', 8}, {'L', 12}}, tot;
    for (int i = 0; i < n; i++) { cin >> s >> l; tot[s] += l; }
    int ans = 0;
    for (auto &c : cap) ans += (tot[c.first] + c.second - 1) / c.second;
    cout << ans << endl;
}
