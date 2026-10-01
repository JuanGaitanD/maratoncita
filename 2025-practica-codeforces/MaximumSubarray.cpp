// Kadane: la mejor suma que termina en i es max(x, mejor_anterior + x). O(n).
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    long long best = LLONG_MIN, cur = 0, x;
    for (int i = 0; i < n; i++) {
        cin >> x;
        cur = max(cur, 0LL) + x;
        best = max(best, cur);
    }
    cout << best << "\n";
}
