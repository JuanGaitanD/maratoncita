// Greedy con dos punteros sobre manos ordenadas: max victorias de Alice = emparejamientos
// donde su carta supera a la de Bob; min de Alice = n - max victorias de Bob.
#include <bits/stdc++.h>
using namespace std;
int wins(const vector<int>& h1, const vector<int>& h2) {
    int w = 0;
    for (int x : h1) if (x > h2[w]) w++;
    return w;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<int> a(n), b; vector<bool> has(2 * n + 1);
    for (int &x : a) { cin >> x; has[x] = true; }
    sort(a.begin(), a.end());
    for (int x = 1; x <= 2 * n; x++) if (!has[x]) b.push_back(x);
    cout << n - wins(b, a) << " " << wins(a, b) << "\n";
}
