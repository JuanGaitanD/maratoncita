// Fuerza bruta sobre (i, j, k) copias de cada pesa: la balanza queda equilibrada si todas
// van al otro platillo o si una sola clase acompana al objeto. O(C^3), C pequeno.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long c, w, t1, t2, t3, r = 0;
    cin >> c >> w >> t1 >> t2 >> t3;
    for (int i = 0; i <= c; i++)
        for (int j = 0; j <= c; j++)
            for (int k = 0; k <= c; k++) {
                long long a = i * t1, b = j * t2, d = k * t3;
                if (a + b + d == w || w + a == b + d || w + b == a + d || w + d == a + b) r++;
            }
    cout << r << "\n";
}
