// Probar todos los a >= 1: (D - a*A) debe ser positivo y divisible por K.
#include <bits/stdc++.h>
int main() {
    int d, A, K, ok = 0; std::cin >> d >> A >> K;
    for (int a = 1; d - a * A > 0; a++) if ((d - a * A) % K == 0) ok = 1;
    std::cout << ok << "\n";
}
