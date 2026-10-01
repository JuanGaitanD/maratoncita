// Un twin de 2m digitos equivale a su "mitad" de m digitos (sin cero inicial).
// f(X) = twins <= X: todos los de longitud menor (10^m - 1) + mitades h con twin(h) <= X.
#include <bits/stdc++.h>
using namespace std;
const int M = 10007;
long long pw(long long b, long long e) { long long r = 1; b %= M; while (e) { if (e & 1) r = r * b % M; b = b * b % M; e >>= 1; } return r; }
long long f(const string &x) {
    int L = x.size();
    long long full = (pw(10, L / 2 - (L % 2 == 0)) - 1 + M) % M;
    if (L % 2) return full;
    int m = L / 2;
    long long h = 0;
    for (int i = 0; i < m; i++) {
        char a = x[2 * i], b = x[2 * i + 1];
        if (a == b) { h = (h * 10 + a - '0') % M; continue; }
        int d = a < b ? a - '0' : a - '0' - 1;
        if (i == 0 && d == 0) return full;
        long long p = pw(10, m - i - 1);
        h = ((h * 10 + d) % M * p + p - 1) % M;
        break;
    }
    return ((full + h - pw(10, m - 1) + 1) % M + M) % M;
}
bool twin(const string &x) {
    if (x.size() % 2) return false;
    for (size_t i = 0; i < x.size(); i += 2) if (x[i] != x[i + 1]) return false;
    return true;
}
int main() {
    string lo, hi; cin >> lo >> hi;
    cout << ((f(hi) - f(lo) + twin(lo)) % M + M) % M << "\n";
}
