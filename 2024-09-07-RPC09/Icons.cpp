// Fila 2 con altura s_j: s_1..s_{j-1} van en fila 1 con s_j..s_{2j-2} de pareja y el resto
// se empareja de a dos consecutivos (ancho s_{2j-1}+s_{2j+1}+...). Probar todo j.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int N; scanf("%d", &N);
    vector<long long> s(2 * N + 1), alt(2 * N + 3, 0);
    for (int i = 1; i <= 2 * N; i++) scanf("%lld", &s[i]);
    for (int i = 2 * N; i >= 1; i--) alt[i] = s[i] + alt[i + 2];
    long long best = LLONG_MAX, pre = 0;
    for (int j = 2; j <= N + 1; j++) {
        pre += s[j - 1];
        best = min(best, (s[1] + s[j]) * (pre + alt[2 * j - 1]));
    }
    printf("%lld\n", best);
}
