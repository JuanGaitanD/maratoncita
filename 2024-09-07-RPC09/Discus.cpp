// Respuesta = max_j a[j] - min(a[j-m..j]); minimo de ventana deslizante con deque.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m; vector<long long> a(n); for (auto &x : a) cin >> x;
    deque<int> q; long long best = 0;
    for (int j = 0; j < n; j++) {
        while (!q.empty() && a[q.back()] >= a[j]) q.pop_back();
        q.push_back(j);
        if (q.front() < j - m) q.pop_front();
        best = max(best, a[j] - a[q.front()]);
    }
    cout << best << "\n";
}
