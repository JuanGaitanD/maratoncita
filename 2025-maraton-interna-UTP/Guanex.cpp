// Cola de prioridad (min-heap): 1 x inserta, 2 elimina el minimo, 3 consulta el minimo.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    priority_queue<long long, vector<long long>, greater<long long> > h;
    while (n--) {
        int op; cin >> op;
        if (op == 1) { long long x; cin >> x; h.push(x); }
        else if (op == 2) { if (!h.empty()) h.pop(); }
        else if (h.empty()) cout << "Empty!\n";
        else cout << h.top() << "\n";
    }
}
