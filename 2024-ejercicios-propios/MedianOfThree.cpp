// Ordenar los tres numeros y tomar el del medio.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long v[3]; cin >> v[0] >> v[1] >> v[2];
        sort(v, v + 3);
        cout << (k ? " " : "") << v[1];
    }
    cout << "\n";
}
