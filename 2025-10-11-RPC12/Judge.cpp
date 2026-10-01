// Marca los dias de vacaciones de cada juez y cuenta dias con >= 3 jueces libres. O(n*m).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m; cin >> n >> m;
    vector<int> fr(m + 1, n);
    for (int j = 0; j < n; j++) {
        int v; cin >> v;
        while (v--) { int s, e; cin >> s >> e; for (int d = s; d <= e; d++) fr[d]--; }
    }
    int c = 0;
    for (int d = 1; d <= m; d++) c += fr[d] >= 3;
    cout << c << endl;
}
