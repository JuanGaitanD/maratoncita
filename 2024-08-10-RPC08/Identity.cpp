// Tela: 4x^2 sin(t) <= a, con t <= pi/4 (paraguas plano). Las puntas forman un octagono
// regular de radio R = x sin(t/2)/sin(pi/8); area seca = 2*sqrt(2)*R^2.
#include <bits/stdc++.h>
using namespace std;
int main() {
    double a, x, PI = acos(-1.0);
    scanf("%lf %lf", &a, &x);
    double s = a / (4 * x * x);
    double t = s >= sin(PI / 4) ? PI / 4 : asin(s);
    double R = x * sin(t / 2) / sin(PI / 8);
    printf("%.10f\n", 2 * sqrt(2.0) * R * R);
}
