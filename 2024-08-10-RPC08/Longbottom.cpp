// Menor k con 32*2^k >= |s|; se imprime "long" k+1 veces.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    long long c = 32; int k = 1;
    while (c < (long long)s.size()) { c *= 2; k++; }
    for (int i = 0; i < k; i++) cout << (i ? " long" : "long");
    cout << "\n";
}
