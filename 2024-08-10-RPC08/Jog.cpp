// Ir a la celda de la ruta mas cercana (Manhattan d) y correr en contra de Jesse:
// se encuentra una fase nueva cada medio segundo. Esperado = d + (n-1)/4.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long x, y, n, m = LLONG_MAX;
    scanf("%lld %lld %lld", &x, &y, &n);
    for (int i = 0; i < n; i++) {
        long long a, b; scanf("%lld %lld", &a, &b);
        m = min(m, llabs(a - x) + llabs(b - y));
    }
    long long v = 4 * m + n - 1;  // respuesta * 4, exacta
    printf("%lld.%02lld\n", v / 4, v % 4 * 25);
}
