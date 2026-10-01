// Costo por pagina = min(alternar diferencias, 1+no deseados (Select All), 1+deseados (Deselect All)).
// Navegacion: cubrir [min,max] de paginas con trabajo desde s: (R-L) + min(|s-L|,|s-R|).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m, s, p, q; cin >> n >> m >> s >> p >> q;
    vector<int> pre(n + 1), want(n + 1);
    for (int i = 0, x; i < p; i++) { cin >> x; pre[x] = 1; }
    for (int i = 0, x; i < q; i++) { cin >> x; want[x] = 1; }
    int pages = (n + m - 1) / m, total = 0, L = -1, R = -1;
    for (int g = 1; g <= pages; g++) {
        int a = (g - 1) * m + 1, b = min(n, g * m), diff = 0, w = 0;
        for (int i = a; i <= b; i++) { diff += pre[i] != want[i]; w += want[i]; }
        if (!diff) continue;
        total += min(diff, min(1 + (b - a + 1) - w, 1 + w));
        if (L < 0) L = g;
        R = g;
    }
    if (L > 0) total += (R - L) + min(abs(s - L), abs(s - R));
    cout << total << endl;
}
