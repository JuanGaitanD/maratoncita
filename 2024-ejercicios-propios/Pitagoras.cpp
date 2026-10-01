// Comparar c^2 con a^2 + b^2 en enteros: igual -> R, menor -> A (agudo), mayor -> O (obtuso).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long a, b, c; cin >> a >> b >> c;
        long long s = a * a + b * b;
        cout << (k ? " " : "") << (c * c == s ? 'R' : (c * c < s ? 'A' : 'O'));
    }
    cout << "\n";
}
