// DP por valor 1..13; estado = largo de la escalera abierta por color (0,1,2,3+), en base 4.
// Cada ficha va a escalera o al grupo del valor; el grupo debe tener 0, 3 o 4 fichas.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    map<string,int> col = {{"Red",0},{"Yellow",1},{"Blue",2},{"Black",3}};
    bool have[14][4] = {};
    for (int i = 0; i < n; i++) { string c; int v; cin >> c >> v; have[v][col[c]] = true; }
    vector<bool> cur(256, false); cur[0] = true;
    for (int v = 1; v <= 13; v++) {
        vector<bool> nxt(256, false);
        for (int st = 0; st < 256; st++) if (cur[st])
            for (int mask = 0; mask < 16; mask++) {  // bit c: la ficha de color c va al grupo
                int g = __builtin_popcount(mask), ns = 0; bool ok = (g == 0 || g >= 3);
                for (int c = 0; c < 4 && ok; c++) {
                    int p = (st >> (2 * c)) & 3, np = 0;
                    bool closed = (p == 0 || p == 3);
                    if (mask >> c & 1) { if (!have[v][c] || !closed) ok = false; }
                    else if (have[v][c]) np = min(p + 1, 3);
                    else if (!closed) ok = false;
                    ns |= np << (2 * c);
                }
                if (ok) nxt[ns] = true;
            }
        cur = nxt;
    }
    bool ok = false;
    for (int st = 0; st < 256; st++) if (cur[st]) {
        bool e = true;
        for (int c = 0; c < 4; c++) { int p = (st >> (2 * c)) & 3; if (p == 1 || p == 2) e = false; }
        if (e) ok = true;
    }
    cout << (ok ? "possible" : "impossible") << "\n";
}
