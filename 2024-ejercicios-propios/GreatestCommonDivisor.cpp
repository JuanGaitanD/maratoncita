// Euclides para el MCD; MCM = a / mcd * b.
#include <bits/stdc++.h>
using namespace std;
long long g(long long a, long long b) { return b ? g(b, a % b) : a; }
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        long long a, b; cin >> a >> b;
        long long d = g(a, b);
        cout << (k ? " " : "") << "(" << d << " " << a / d * b << ")";
    }
    cout << "\n";
}
