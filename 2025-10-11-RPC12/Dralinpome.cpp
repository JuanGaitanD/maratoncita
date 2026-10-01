// Se puede formar palindromo si a lo sumo una letra aparece un numero impar de veces.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    int c[26] = {0}, odd = 0;
    for (char ch : s) c[ch - 'a']++;
    for (int i = 0; i < 26; i++) odd += c[i] & 1;
    cout << (odd <= 1 ? "yes" : "no") << endl;
}
