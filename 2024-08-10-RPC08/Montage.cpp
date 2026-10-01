// Posible si y solo si ninguna altura se repite mas de w veces (w columnas estrictas).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, w; scanf("%d %d", &n, &w);
    vector<int> h(n);
    for (auto &x : h) scanf("%d", &x);
    sort(h.begin(), h.end());
    bool ok = true;
    for (int i = 0; i + w < n; i++) if (h[i] == h[i + w]) ok = false;
    puts(ok ? "yes" : "no");
}
