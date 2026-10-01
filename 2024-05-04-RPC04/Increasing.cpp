// Recorrido lineal: longitud de la racha estrictamente creciente actual.
#include <bits/stdc++.h>
int main() {
    int n; std::cin >> n; std::vector<int> v(n);
    for (auto &x : v) std::cin >> x;
    int best = 1, cur = 1;
    for (int i = 1; i < n; i++) { cur = v[i] > v[i - 1] ? cur + 1 : 1; best = std::max(best, cur); }
    std::cout << best << "\n";
}
