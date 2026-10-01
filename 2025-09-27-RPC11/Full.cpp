// Full house: las frecuencias de los digitos ordenadas son exactamente [2, 3].
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    map<char, int> f;
    for (char ch : s) f[ch]++;
    vector<int> v;
    for (auto &e : f) v.push_back(e.second);
    sort(v.begin(), v.end());
    cout << (v == vector<int>{2, 3} ? "YES" : "NO") << "\n";
}
