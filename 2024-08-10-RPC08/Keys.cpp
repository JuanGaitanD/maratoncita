// Una tecla por cada cambio de letra (sin importar mayuscula) o espacio, mas un shift
// por cada bloque de mayusculas (los espacios no rompen el bloque, las minusculas si).
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; getline(cin, s);
    if (!s.empty() && s.back() == '\r') s.pop_back();
    int cost = 0; char prev = 0; bool shift = false;
    for (char ch : s) {
        char k = tolower(ch);
        if (k != prev) cost++;
        prev = k;
        if (isupper(ch)) { if (!shift) { cost++; shift = true; } }
        else if (islower(ch)) shift = false;
    }
    cout << cost << "\n";
}
