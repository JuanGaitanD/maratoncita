// A(psi) = area libre con angulo en [-theta, psi] = R^2/2*(psi+theta) - parte de cada circulo
// del lado "angulo < psi" de la recta por el origen (segmento circular). A es creciente:
// biseccion para cada objetivo j*Total/k.
#include <bits/stdc++.h>
using namespace std;
int n, k; double R, th;
vector<double> LO, HI, RR, F, D, AR;
double area(double psi) {
    double s = R * R / 2 * (psi + th);
    for (int i = 0; i < n; i++) {
        if (psi >= HI[i]) s -= AR[i];
        else if (psi > LO[i]) {
            double d = D[i], t = RR[i] * sin(F[i] - psi);
            t = max(-d, min(d, t));
            s -= d * d * acos(t / d) - t * sqrt(d * d - t * t);
        }
    }
    return s;
}
int main() {
    double deg;
    cin >> n >> k >> R >> deg;
    th = deg * M_PI / 180;
    double total = R * R * th;
    for (int i = 0; i < n; i++) {
        double r, f, d; cin >> r >> f >> d;
        f = f * M_PI / 180; d /= 2;
        double a = asin(d / r);
        LO.push_back(f - a); HI.push_back(f + a); RR.push_back(r); F.push_back(f); D.push_back(d);
        AR.push_back(M_PI * d * d); total -= M_PI * d * d;
    }
    double lo = -th;
    for (int j = 1; j < k; j++) {
        double goal = total * j / k, a = lo, b = th;
        for (int it = 0; it < 55; it++) {
            double m = (a + b) / 2;
            if (area(m) < goal) a = m; else b = m;
        }
        lo = a;
        double x = a * 180 / M_PI;
        if (fabs(x) <= 5e-11) x = 0;
        printf("%.10f\n", x);
    }
}
