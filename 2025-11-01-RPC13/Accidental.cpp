// Solo el primer termino tiene signo esperado no nulo (+/- equiprobables se cancelan).
// Si el primer termino acaba en el digito j aporta S_j = sum_{i<=j} d_i*10^-i (prob 0.9, o 1 si es el ultimo).
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    double acc = 0, p = 1, e = 0;
    for (size_t i = 0; i < s.size(); i++) {
        acc += (s[i] - '0') * p;
        p /= 10;
        e += acc * (i + 1 < s.size() ? 0.9 : 1.0);
    }
    printf("%.9f\n", e);
}
