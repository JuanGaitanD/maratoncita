// Recorrer todos los numeros guardando maximo y minimo.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long x, mx = LLONG_MIN, mn = LLONG_MAX;
    while (cin >> x) { mx = max(mx, x); mn = min(mn, x); }
    cout << mx << " " << mn << "\n";
}
