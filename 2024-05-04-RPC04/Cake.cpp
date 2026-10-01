// Area doble total S (shoelace). Para cada diagonal (i, j) no adyacente, la pieza i..j tiene
// area doble P; diferencia = |S - 2P| / 2. O(n^3) con n <= 100 basta.
#include <bits/stdc++.h>
using namespace std;
int n;
long long X[100], Y[100];
long long area(int i, int j) {
    long long s = 0;
    for (int t = i; t <= j; t++) { int u = t == i ? j : t - 1; s += X[t] * Y[u] - X[u] * Y[t]; }
    return llabs(s);
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> X[i] >> Y[i];
    long long S = area(0, n - 1), best = LLONG_MAX;
    for (int i = 0; i < n; i++)
        for (int j = i + 2; j < n; j++)
            if (!(i == 0 && j == n - 1)) best = min(best, llabs(S - 2 * area(i, j)));
    cout << best / 2 << '.' << 5 * (best % 2) << "\n";
}
