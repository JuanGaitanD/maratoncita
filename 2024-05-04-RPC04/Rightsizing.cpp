// Set ordenado por (-salario, nombre); un aumento borra y reinserta, despedir toma el primero.
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, a; cin >> n >> a;
    map<string, long long> sal;
    set<pair<long long, string>> st;
    for (int i = 0; i < n; i++) { string e; long long s; cin >> e >> s; sal[e] = s; st.insert({-s, e}); }
    while (a--) {
        int t; cin >> t;
        if (t == 1) {
            string e; long long r; cin >> e >> r;
            st.erase({-sal[e], e}); sal[e] += r; st.insert({-sal[e], e});
        } else {
            auto it = st.begin();
            cout << it->second << ' ' << -it->first << '\n';
            sal.erase(it->second); st.erase(it);
        }
    }
}
