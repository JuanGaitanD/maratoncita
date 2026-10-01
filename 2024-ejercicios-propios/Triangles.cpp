// Hay triangulo si cada lado es menor que la suma de los otros dos.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long a, b, c; cin >> a >> b >> c;
        cout << (k ? " " : "") << (a + b > c && a + c > b && b + c > a ? 1 : 0);
    }
    cout << "\n";
}
