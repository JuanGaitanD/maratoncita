// Volumenes tras d dias (sin bajar de 0) y porcentaje de alcohol.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long d, a, o, da, dO; cin >> d >> a >> o >> da >> dO;
    a = max(0LL, a - d * da); o = max(0LL, o - d * dO);
    printf("%.10f\n", 100.0 * (double)a / (double)(a + o));
}
