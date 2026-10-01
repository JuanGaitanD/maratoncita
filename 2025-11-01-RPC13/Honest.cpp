// Contar apariciones de cada numero y listar los que superan 2n.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, x;
    cin >> n;
    vector<int> cnt(51, 0);
    for (int i = 0; i < 50 * n; i++) { cin >> x; cnt[x]++; }
    string out;
    for (int v = 1; v <= 50; v++)
        if (cnt[v] > 2 * n) out += (out.empty() ? "" : " ") + to_string(v);
    cout << (out.empty() ? "-1" : out) << endl;
}
