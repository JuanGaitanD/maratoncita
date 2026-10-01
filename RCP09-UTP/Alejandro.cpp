// Se simula el algoritmo: letra original = cifrada - c; se cuenta la original y si su cuenta es multiplo de K, c sube.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; long long k; cin >> n >> k;
    long long cnt[26] = {0}, c = 0;
    string w, out;
    for (int t = 0; t < n; t++) {
        cin >> w;
        for (char &ch : w) {
            int L = ((ch - 'a' - c) % 26 + 26) % 26;
            ch = 'a' + L;
            if (++cnt[L] % k == 0) c++;
        }
        if (t) out += ' ';
        out += w;
    }
    cout << out << "\n";
}
