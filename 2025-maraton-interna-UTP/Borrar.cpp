// Quitar los caracteres prohibidos (dados entre corchetes) y no repetir un caracter igual
// al ultimo que quedo en el resultado; al final recortar espacios de los extremos.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string text, oc, res;
    getline(cin, text); getline(cin, oc);
    if (!text.empty() && text.back() == '\r') text.pop_back();
    while (!oc.empty() && isspace((unsigned char)oc.back())) oc.pop_back();
    set<char> banned(oc.begin() + 1, oc.end() - 1);
    for (char ch : text)
        if (!banned.count(ch) && (res.empty() || res.back() != ch)) res += ch;
    size_t a = res.find_first_not_of(" \t"), b = res.find_last_not_of(" \t");
    cout << (a == string::npos ? "" : res.substr(a, b - a + 1)) << "\n";
}
