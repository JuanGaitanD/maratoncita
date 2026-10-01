// Cada paso fija m mod (n-i) = posicion de la letra en la lista restante.
// CRT incremental con modulos no coprimos: se prueba t en a + M*t (k <= 20 intentos).
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    string s;
    cin >> n >> s;
    string rest;
    for (int i = 0; i < n; i++) rest += char('A' + i);
    long long a = 0, M = 1;
    for (char ch : s) {
        long long k = rest.size(), r = rest.find(ch);
        rest.erase(r, 1);
        int t = 0;
        while (t < k && (a + M * t) % k != r) t++;
        if (t == k) { puts("NO"); return 0; }
        a += M * t;
        M = M / __gcd(M, k) * k;
    }
    printf("YES\n%lld\n", a);
}
