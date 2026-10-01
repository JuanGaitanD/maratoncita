// El volumen hasta altura x es proporcional a rho(x)^3 - r^3 (cono extendido), con rho lineal en x:
// rho^3 = (r^3 + R^3) / 2  ->  x = h (rho - r) / (R - r); si r == R, x = h / 2.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        double r, R, h, x; scanf("%lf %lf %lf", &r, &R, &h);
        if (R - r < 1e-12) x = h / 2;
        else x = h * (cbrt((r*r*r + R*R*R) / 2) - r) / (R - r);
        printf("%.9f\n", x);
    }
}
