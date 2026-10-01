// Propagacion con cola: en cada triangulo (padre, hijo izq, hijo der) si se conocen dos valores
// se deduce el tercero. Contradiccion o valor fuera de [-99,99] -> no solution; si queda
// alguna casilla vacia -> ambiguous.
#include <bits/stdc++.h>
using namespace std;
const int E = 100;
int n; vector<vector<int>> v; deque<pair<int,int>> q;
void addTris(int i, int j) {
    if (i < n - 1) q.push_back({i, j});
    if (i > 0) { if (j < i) q.push_back({i - 1, j}); if (j > 0) q.push_back({i - 1, j - 1}); }
}
int main() {
    cin >> n; v.resize(n);
    for (int i = 0; i < n; i++) { v[i].resize(i + 1); for (auto &x : v[i]) cin >> x; }
    for (int i = 0; i < n - 1; i++) for (int j = 0; j <= i; j++) q.push_back({i, j});
    bool bad = false;
    while (!q.empty() && !bad) {
        int i = q.front().first, j = q.front().second; q.pop_front();
        int &P = v[i][j], &A = v[i + 1][j], &B = v[i + 1][j + 1];
        int known = (P != E) + (A != E) + (B != E);
        if (known == 3) { if (P != A + B) bad = true; continue; }
        if (known < 2) continue;
        int ci, cj, val;
        if (P == E) { ci = i; cj = j; val = A + B; }
        else if (A == E) { ci = i + 1; cj = j; val = P - B; }
        else { ci = i + 1; cj = j + 1; val = P - A; }
        if (val < -99 || val > 99) { bad = true; break; }
        v[ci][cj] = val; addTris(ci, cj);
    }
    if (bad) { cout << "no solution\n"; return 0; }
    for (auto &r : v) for (int x : r) if (x == E) { cout << "ambiguous\n"; return 0; }
    cout << "solvable\n";
    for (auto &r : v) for (size_t j = 0; j < r.size(); j++) cout << r[j] << (j + 1 < r.size() ? ' ' : '\n');
}
