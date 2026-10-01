// DP de abajo hacia arriba: costo minimo para que cada nodo valga T y para que valga F.
// AND: T = suma, F = minimo; OR: T = minimo, F = suma. Hoja: 0 si ya tiene ese valor, 1 si no.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; char t; cin >> n >> t;
    vector<vector<string>> lv(n);
    long long cnt = 1;
    for (int i = 0; i < n; i++) {
        lv[i].resize(cnt); long long nx = 0;
        for (auto &e : lv[i]) { cin >> e; if (e != "T" && e != "F") nx += stoi(e); }
        cnt = nx;
    }
    vector<pair<int,int>> below;
    for (int i = n - 1; i >= 0; i--) {
        bool isAnd = (t == 'A') == (i % 2 == 0);
        vector<pair<int,int>> cur; size_t k = 0;
        for (auto &e : lv[i]) {
            if (e == "T") cur.push_back({0, 1});
            else if (e == "F") cur.push_back({1, 0});
            else {
                int v = stoi(e), st = 0, sf = 0, mt = INT_MAX, mf = INT_MAX;
                for (int j = 0; j < v; j++, k++) {
                    st += below[k].first; sf += below[k].second;
                    mt = min(mt, below[k].first); mf = min(mf, below[k].second);
                }
                cur.push_back(isAnd ? make_pair(st, mf) : make_pair(mt, sf));
            }
        }
        below = cur;
    }
    cout << max(below[0].first, below[0].second) << endl;
}
