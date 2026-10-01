// Se agrupan columnas no vacias consecutivas: 4 columnas = 'v', 8 = 'w'.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; string a, b; cin >> n >> a >> b;
    string res; int run = 0;
    for (int i = 0; i <= n; i++) {
        if (i < n && (a[i] != '.' || b[i] != '.')) run++;
        else if (run) { res += run == 4 ? 'v' : 'w'; run = 0; }
    }
    cout << res << endl;
}
