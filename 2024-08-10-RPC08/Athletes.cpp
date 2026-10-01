// La palabra (en minusculas) debe ser no decreciente o no creciente.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    for (char &c : s) c = tolower(c);
    string a = s, b = s;
    sort(a.begin(), a.end()); sort(b.rbegin(), b.rend());
    cout << (s == a || s == b ? "yes" : "no") << "\n";
}
