// Los pasillos forman un arbol: el nido es su centro (minima excentricidad), el punto medio de un diametro.
// BFS desde cualquier celda -> extremo a; BFS desde a -> extremo b y padres; el centro (o los 2) estan en la mitad.
#include <bits/stdc++.h>
using namespace std;
int W;
string g;
vector<int> par, q;
int bfs(int s) {
    fill(par.begin(), par.end(), -2);
    q.assign(1, s); par[s] = -1;
    for (size_t i = 0; i < q.size(); i++) {
        int v = q[i], nb[4] = {v + 1, v - 1, v + W, v - W};
        for (int u : nb) if (g[u] == '.' && par[u] == -2) { par[u] = v; q.push_back(u); }
    }
    return q.back();
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        int H, Wd; cin >> H >> Wd;
        W = Wd + 2;
        g.assign(W * (H + 2), '#');
        for (int i = 0; i < H; i++) { string s; cin >> s; g.replace((i + 1) * W + 1, Wd, s); }
        par.assign(g.size(), -2);
        int a = bfs(g.find('.'));
        int b = bfs(a);
        vector<int> path = {b};
        while (par[path.back()] != -1) path.push_back(par[path.back()]);
        int L = path.size() - 1, c1 = path[L / 2], c2 = path[(L + 1) / 2];
        pair<int,int> best = min(make_pair(c1 % W, c1 / W), make_pair(c2 % W, c2 / W));
        cout << "Case " << cs << ": " << best.second << " " << best.first << "\n";
    }
}
