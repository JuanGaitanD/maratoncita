// Greedy: el siguiente ganador w es el unico cuyo numero esta al frente de las dos listas
// donde aparece (las de los otros dos jugadores). O(total).
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s[3]; cin >> s[0] >> s[1] >> s[2];
    size_t p[3] = {0, 0, 0};
    size_t total = (s[0].size() + s[1].size() + s[2].size()) / 2;
    auto head = [&](int i) { return p[i] < s[i].size() ? s[i][p[i]] : ' '; };
    string out;
    for (size_t k = 0; k < total; k++)
        for (int w = 0; w < 3; w++) {
            int a = (w + 1) % 3, b = (w + 2) % 3; char c = '1' + w;
            if (head(a) == c && head(b) == c) { p[a]++; p[b]++; out += c; break; }
        }
    cout << out << endl;
}
