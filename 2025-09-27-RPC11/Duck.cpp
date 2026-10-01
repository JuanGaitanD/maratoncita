// Con n = total/3 equipos, se puede repartir sii ningun color tiene mas de n patos.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int c, x, mx = 0, s = 0;
    cin >> c;
    while (c--) { cin >> x; s += x; mx = max(mx, x); }
    cout << (3 * mx <= s ? "YES" : "NO") << "\n";
}
