// Grafo de nombres padre->hijo. La raiz debe ser el unico nombre que es padre y nunca hijo
// (si no hay, un nodo que alcance a todos); posible si desde ella se alcanzan todos los nombres.
#include <bits/stdc++.h>
using namespace std;
map<string, int> idx; vector<vector<int>> adj; vector<int> isChild;
int get(const string &s) {
    auto it = idx.find(s);
    if (it != idx.end()) return it->second;
    adj.push_back({}); isChild.push_back(0);
    return idx[s] = adj.size() - 1;
}
int main() {
    int n; cin >> n;
    for (int k = 0; k < n; k++) {
        string A, so, of, B; cin >> A >> so >> of >> B;
        int a = get(A.substr(0, A.size() - 1)), b = get(B);
        adj[b].push_back(a); isChild[a] = 1;
    }
    int V = adj.size(), r = -1, cnt = 0;
    for (int v = 0; v < V; v++) if (!isChild[v]) { r = v; cnt++; }
    if (cnt > 1) { cout << "impossible" << endl; return 0; }
    if (cnt == 0) {  // ultimo nodo en terminar un DFS
        vector<int> seen(V), it(V);
        for (int s = 0; s < V; s++) {
            if (seen[s]) continue;
            seen[s] = 1; vector<int> st = {s};
            while (!st.empty()) {
                int v = st.back();
                if (it[v] < (int)adj[v].size()) {
                    int u = adj[v][it[v]++];
                    if (!seen[u]) { seen[u] = 1; st.push_back(u); }
                } else { st.pop_back(); r = v; }
            }
        }
    }
    vector<int> seen(V), st = {r}; seen[r] = 1; int c = 1;
    while (!st.empty()) {
        int v = st.back(); st.pop_back();
        for (int u : adj[v]) if (!seen[u]) { seen[u] = 1; c++; st.push_back(u); }
    }
    cout << (c == V ? "possible" : "impossible") << endl;
}
