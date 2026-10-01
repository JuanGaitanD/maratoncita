// Puntaje = 100 - 10 * (distancia de Chebyshev al centro), minimo 0.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, r, c;
    cin >> n >> r >> c;
    int o = n / 2 + 1;
    cout << max(0, 100 - 10 * max(abs(r - o), abs(c - o))) << endl;
}
