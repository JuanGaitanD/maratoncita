// Para cada r se resuelve la cuadratica en g: p*g^2 + (p(2r-1) - 2rq)*g + p(r^2-r) = 0.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long p, q; cin >> p >> q;
    for (long long r = 1; r <= 1000000; r++) {
        long long b = p * (2 * r - 1) - 2 * r * q;
        long long disc = b * b - 4 * p * p * (r * r - r);
        if (disc < 0) continue;
        long long s = (long long)sqrtl((long double)disc);
        while (s * s > disc) s--;
        while ((s + 1) * (s + 1) <= disc) s++;
        if (s * s != disc) continue;
        long long num = -b + s;
        if (num % (2 * p) == 0 && num / (2 * p) >= r) { cout << r << " " << num / (2 * p) << endl; return 0; }
    }
    cout << "impossible" << endl;
}
