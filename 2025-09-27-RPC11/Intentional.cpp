// Cada problema con numero impar de paginas deja una pagina en blanco.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int p, x, c = 0;
    cin >> p;
    while (p--) { cin >> x; c += x % 2; }
    cout << c << "\n";
}
