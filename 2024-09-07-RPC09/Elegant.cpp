// Con t = h/w: madera = w*f(t), area = 1.5*w^2*t  =>  area = 1.5*t*n^2/f(t)^2. Ternaria en t.
#include <bits/stdc++.h>
double n;
double g(double t) {
    double f = 2 + 2 * t + 2 * sqrt(1 + t * t) + 2 * sqrt(0.25 + t * t);
    return 1.5 * t * n * n / (f * f);
}
int main() {
    std::cin >> n; double lo = 0, hi = 10;
    for (int i = 0; i < 200; i++) {
        double a = lo + (hi - lo) / 3, b = hi - (hi - lo) / 3;
        if (g(a) < g(b)) lo = a; else hi = b;
    }
    printf("%.10f\n", g(lo));
}
