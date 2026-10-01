// Imprimir el menor de cada par.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long a, b; cin >> a >> b;
        cout << (k ? " " : "") << min(a, b);
    }
    cout << "\n";
}
