// Backtracking: el punto libre de menor indice forma triangulo con otros dos libres.
// Areas dobles enteras; se poda si (max - min) ya no mejora. Respuesta = D/2 exacta.
#include <bits/stdc++.h>
using namespace std;
int N;
long long X[15], Y[15], best = LLONG_MAX;
long long ar(int i, int j, int k) { return llabs((X[j] - X[i]) * (Y[k] - Y[i]) - (X[k] - X[i]) * (Y[j] - Y[i])); }
void go(int used, long long lo, long long hi) {
    if (hi - lo >= best) return;
    if (used == (1 << N) - 1) { best = hi - lo; return; }
    int i = 0;
    while (used >> i & 1) i++;
    for (int j = i + 1; j < N; j++) if (!(used >> j & 1))
        for (int k = j + 1; k < N; k++) if (!(used >> k & 1)) {
            long long a = ar(i, j, k);
            go(used | 1 << i | 1 << j | 1 << k, min(lo, a), max(hi, a));
        }
}
int main() {
    int n; cin >> n; N = 3 * n;
    for (int i = 0; i < N; i++) cin >> X[i] >> Y[i];
    go(0, LLONG_MAX / 4, -LLONG_MAX / 4);
    cout << best / 2 << '.' << 5 * (best % 2) << "\n";
}
