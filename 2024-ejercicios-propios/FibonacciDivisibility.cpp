// Para cada M, avanzamos Fibonacci modulo M hasta encontrar F(i) % M == 0 con i > 0.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long m; cin >> m;
        long long a = 1 % m, b = 1 % m, i = 1;
        while (a) { long long c = (a + b) % m; a = b; b = c; i++; }
        cout << (k ? " " : "") << i;
    }
    cout << "\n";
}
