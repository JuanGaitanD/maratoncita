// El bloque i tiene i terminos; se busca i con i(i-1)/2 < n <= i(i+1)/2 y k = n - i(i-1)/2 - 1.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n; cin >> n;
    long long i = (long long)sqrt(2.0L * n) + 2;
    while (i * (i - 1) / 2 >= n) i--;
    long long k = n - i * (i - 1) / 2 - 1;
    if (k == 0) cout << i << endl;
    else { long long g = __gcd(k, i); cout << i << " " << k / g << "/" << i / g << endl; }
}
