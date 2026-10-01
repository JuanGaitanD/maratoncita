// Para cada vector v = P - A: B debe cumplir B.v = A.v y C debe cumplir C.v = P.v = A.v + |v|^2.
// Por cada v con algun par (A, P): histogramas de B.v y C.v y se suma cntB[A.v] * cntC[A.v + |v|^2].
#include <bits/stdc++.h>
using namespace std;
int n;
char g[22][22][23];
int main() {
    scanf("%d", &n);
    char buf[64];
    vector<array<int, 3> > Bs, Cs;
    for (int z = 0; z < n; z++) {
        scanf("%s", buf);  // "-"
        for (int y = 0; y < n; y++) {
            scanf("%s", g[z][y]);
            for (int x = 0; x < n; x++) {
                array<int, 3> p = {{x, y, z}};
                if (g[z][y][x] == 'B') Bs.push_back(p);
                if (g[z][y][x] == 'C') Cs.push_back(p);
            }
        }
    }
    const int OFF = 3000;
    vector<long long> hb(6001, 0), hc(6001, 0);
    vector<int> keys;
    long long ans = 0;
    for (int dx = -n + 1; dx < n; dx++)
        for (int dy = -n + 1; dy < n; dy++)
            for (int dz = -n + 1; dz < n; dz++) {
                if (!dx && !dy && !dz) continue;
                keys.clear();
                for (int z = max(0, -dz); z < n - max(0, dz); z++)
                    for (int y = max(0, -dy); y < n - max(0, dy); y++)
                        for (int x = max(0, -dx); x < n - max(0, dx); x++)
                            if (g[z][y][x] == 'A' && g[z + dz][y + dy][x + dx] == 'P')
                                keys.push_back(x * dx + y * dy + z * dz);
                if (keys.empty()) continue;
                for (auto &p : Bs) hb[p[0] * dx + p[1] * dy + p[2] * dz + OFF]++;
                for (auto &p : Cs) hc[p[0] * dx + p[1] * dy + p[2] * dz + OFF]++;
                int vv = dx * dx + dy * dy + dz * dz;
                for (int k : keys) ans += hb[k + OFF] * hc[k + vv + OFF];
                for (auto &p : Bs) hb[p[0] * dx + p[1] * dy + p[2] * dz + OFF] = 0;
                for (auto &p : Cs) hc[p[0] * dx + p[1] * dy + p[2] * dz + OFF] = 0;
            }
    printf("%lld\n", ans);
}
