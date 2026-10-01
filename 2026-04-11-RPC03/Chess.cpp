// Backtracking probando capturas en orden lexicografico (origen, destino); la primera
// secuencia completa encontrada es la pedida. Se memorizan los estados sin solucion.
#include <bits/stdc++.h>
using namespace std;
int n, m;
set<map<pair<int,int>, char>> dead;
vector<string> path;
string nm(pair<int,int> c) { return string(1, 'A' + c.first) + char('1' + c.second); }
int KN[8][2] = {{1,2},{2,1},{-1,2},{-2,1},{1,-2},{2,-1},{-1,-2},{-2,-1}};
int DR[8][2] = {{1,1},{1,-1},{-1,1},{-1,-1},{1,0},{-1,0},{0,1},{0,-1}};
vector<pair<int,int>> caps(map<pair<int,int>, char> &b, pair<int,int> c) {
    char p = b[c]; vector<pair<int,int>> out;
    if (p == 'N' || p == 'K') {
        for (int i = 0; i < 8; i++) {
            int dr = p == 'N' ? KN[i][0] : DR[i][0], dc = p == 'N' ? KN[i][1] : DR[i][1];
            pair<int,int> t(c.first + dr, c.second + dc);
            if (b.count(t)) out.push_back(t);
        }
    } else {
        int lo = p == 'R' ? 4 : 0, hi = p == 'B' ? 4 : 8;
        for (int i = lo; i < hi; i++) {
            int r = c.first + DR[i][0], k = c.second + DR[i][1];
            while (r >= 0 && r < n && k >= 0 && k < n) {
                if (b.count({r, k})) { out.push_back({r, k}); break; }
                r += DR[i][0]; k += DR[i][1];
            }
        }
    }
    return out;
}
bool solve(map<pair<int,int>, char> b) {
    if (b.size() == 1) return true;
    if (dead.count(b)) return false;
    vector<tuple<string,string,pair<int,int>,pair<int,int>>> mv;
    for (auto &e : b) for (auto t : caps(b, e.first)) mv.push_back(make_tuple(nm(e.first), nm(t), e.first, t));
    sort(mv.begin(), mv.end());
    for (auto &x : mv) {
        auto nb = b; pair<int,int> c = get<2>(x), t = get<3>(x);
        nb[t] = nb[c]; nb.erase(c);
        path.push_back(string(1, b[c]) + ": " + get<0>(x) + " -> " + get<1>(x));
        if (solve(nb)) return true;
        path.pop_back();
    }
    dead.insert(b);
    return false;
}
int main() {
    cin >> n >> m; map<pair<int,int>, char> b;
    for (int i = 0; i < m; i++) { char p; string loc; cin >> p >> loc; b[{loc[0] - 'A', loc[1] - '1'}] = p; }
    if (solve(b)) for (auto &s : path) cout << s << "\n";
    else cout << "No solution\n";
}
