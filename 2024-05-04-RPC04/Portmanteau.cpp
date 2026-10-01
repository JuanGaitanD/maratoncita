// Simulacion directa de las reglas: prefijo hasta la primera vocal (desde la 2a letra),
// sufijo hasta la primera vocal hacia la izquierda, y vocal de union v2, v1 u 'o'.
#include <bits/stdc++.h>
using namespace std;
bool isv(char c) { return string("aeiou").find(c) != string::npos; }
int main() {
    string a, b; cin >> a >> b;
    int i = 1, j = (int)b.size() - 2;
    while (i < (int)a.size() && !isv(a[i])) i++;
    while (j >= 0 && !isv(b[j])) j--;
    char m = j >= 0 ? b[j] : (i < (int)a.size() ? a[i] : 'o');
    cout << a.substr(0, i) + m + b.substr(j + 1) << "\n";
}
