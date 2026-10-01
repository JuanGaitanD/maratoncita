// a = menor/3 y c = mayor/3; se prueba cada b y se compara el conjunto de sumas de 3 saltos con la lista.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> d(n);
    for (int &x : d) cin >> x;
    set<int> target(d.begin(), d.end());
    int a = d[0] / 3, c = d[n - 1] / 3;
    for (int b = a + 1; b < c; b++) {
        int v[3] = {a, b, c};
        set<int> s;
        for (int i = 0; i < 3; i++)
            for (int j = i; j < 3; j++)
                for (int k = j; k < 3; k++) s.insert(v[i] + v[j] + v[k]);
        if (s == target) { printf("%d %d %d\n", a, b, c); break; }
    }
}
