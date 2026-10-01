// Casa = rectangulo w*t x h*t centrado en (x, y). Para un centro fijo, el t maximo es el
// minimo sobre los 4 lados de una funcion lineal -> concava; ternaria anidada en x e y.
#include <bits/stdc++.h>
using namespace std;
double A[4], B[4], C[4], K[4];
double bestT(double x, double y) {
    double r = 1e18;
    for (int i = 0; i < 4; i++) r = min(r, (C[i] - A[i] * x - B[i] * y) / K[i]);
    return r;
}
template <class F> double tern(double lo, double hi, F g) {
    for (int it = 0; it < 100; it++) {
        double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
        if (g(m1) < g(m2)) lo = m1; else hi = m2;
    }
    return g((lo + hi) / 2);
}
int main() {
    double x[4], y[4], w, h, gx = 0, gy = 0;
    for (int i = 0; i < 4; i++) { cin >> x[i] >> y[i]; gx += x[i] / 4; gy += y[i] / 4; }
    cin >> w >> h;
    for (int i = 0; i < 4; i++) {
        int j = (i + 1) % 4;
        double a = y[j] - y[i], b = x[i] - x[j], c = a * x[i] + b * y[i];
        if (a * gx + b * gy > c) { a = -a; b = -b; c = -c; }
        A[i] = a; B[i] = b; C[i] = c; K[i] = (fabs(a) * w + fabs(b) * h) / 2;
    }
    double x0 = *min_element(x, x + 4), x1 = *max_element(x, x + 4);
    double y0 = *min_element(y, y + 4), y1 = *max_element(y, y + 4);
    double t = tern(x0, x1, [&](double cx) { return tern(y0, y1, [&](double cy) { return bestT(cx, cy); }); });
    t = max(t, 0.0);
    printf("%.9f\n", w * h * t * t);
}
