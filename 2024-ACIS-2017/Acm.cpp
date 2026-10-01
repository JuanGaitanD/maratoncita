// Sumar las longitudes de los tramos de cada punto de partida; el equipo camina a la
// velocidad del mas lento. Respuesta: min sobre puntos de ceil(suma / vmin). Varios casos hasta EOF.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string line;
    while (getline(cin, line)) {
        istringstream h(line); long long n, s;
        if (!(h >> n >> s)) break;
        map<long long, long long> tot;
        for (int i = 0; i < s; i++) {
            getline(cin, line); istringstream r(line);
            long long a, b, d; r >> a >> b >> d; tot[a] += d;
        }
        getline(cin, line); istringstream r(line);
        long long v = LLONG_MAX, x;
        while (r >> x) v = min(v, x);
        long long best = LLONG_MAX;
        for (auto &e : tot) best = min(best, (e.second + v - 1) / v);
        cout << best << "\n";
    }
}
