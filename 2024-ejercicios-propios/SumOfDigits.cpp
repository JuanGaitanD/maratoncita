// Calcular a*b+c y sumar sus digitos.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long a, b, c; cin >> a >> b >> c;
        long long v = a * b + c, s = 0;
        for (; v > 0; v /= 10) s += v % 10;
        cout << (k ? " " : "") << s;
    }
    cout << "\n";
}
