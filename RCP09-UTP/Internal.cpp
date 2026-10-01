// Triangulos con 3 vertices del n-gono convexo: C(n, 3) mod 1e9+7, usando el inverso modular de 6.
#include <bits/stdc++.h>
using namespace std;
const long long M = 1000000007, INV6 = 166666668;
int main() {
    int q; scanf("%d", &q);
    while (q--) {
        long long n; scanf("%lld", &n);
        long long a = n % M, b = (n - 1) % M, c = (n - 2) % M;
        printf("%lld\n", a * b % M * c % M * INV6 % M);
    }
}
