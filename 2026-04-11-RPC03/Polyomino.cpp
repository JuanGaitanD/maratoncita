// Beauquier-Nivat: B = X Y Xb Yb o X Y Z Xb Yb Zb (Xb = reverso complementado), h = k/2.
// Arcos buenos expandidos desde cada centro; cadenas de 2 y 3 arcos que suman h con bitsets.
#include <bits/stdc++.h>
using namespace std;
const int MH = 5001;
bitset<MH> outb[5000], rin[5000];
int main() {
    int k; string s; cin >> k >> s;
    if (k % 2) { cout << 0 << endl; return 0; }
    int h = k / 2;
    auto comp = [](char c) { return c == 'u' ? 'd' : c == 'd' ? 'u' : c == 'l' ? 'r' : 'l'; };
    auto md = [&](long long x, int M) { return (int)(((x % M) + M) % M); };
    auto match = [&](int i, int S) { return comp(s[md(i, k)]) == s[md(S - i, k)]; };
    for (int c2 = 0; c2 < k; c2++) {
        int S = c2 + h, l = c2 / 2, r = c2 % 2 ? l + 1 : l;
        bool ok = match(l, S) && (l == r || match(r, S));
        while (ok && r - l + 1 < h) {
            int L = r - l + 1, q = md(l, h);
            outb[q][L] = 1; rin[(q + L) % h][h - L] = 1;
            l--; r++;
            ok = match(l, S) && match(r, S);
        }
    }
    long long tot = 0;
    for (int q1 = 0; q1 < h; q1++)
        for (int a = 1; a < h; a++) if (outb[q1][a]) {
            const bitset<MH> &o2 = outb[(q1 + a) % h];
            tot += o2[h - a] + (o2 & (rin[q1] >> a)).count();
        }
    cout << 2 * tot << endl;
}
