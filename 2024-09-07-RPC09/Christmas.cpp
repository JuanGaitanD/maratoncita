// Cuerda 2r*sin(phi/2) <= l  <=>  phi <= 2*asin(l/2r); phi uniforme en [0,pi].
#include <bits/stdc++.h>
int main() {
    long long r, l; std::cin >> r >> l;
    double p = l >= 2 * r ? 0.0 : 1 - 2 * asin((double)l / (2.0 * r)) / M_PI;
    printf("%.10f\n", p);
}
