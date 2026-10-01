// Burbuja: en cada pasada el mayor restante "sube" al final. O(n^2).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    for (int i = 0; i + 1 < n; i++)
        for (int j = 0; j + 1 < n - i; j++)
            if (a[j] > a[j + 1]) swap(a[j], a[j + 1]);
    for (int i = 0; i < n; i++) cout << (i ? " " : "") << a[i];
    cout << "\n";
}
