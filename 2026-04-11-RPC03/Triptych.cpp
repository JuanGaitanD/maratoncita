// DP por (cuantas A, cuantas B, estado final: A, B simple, BB, C). Se cuentan las validas y se
// restan los palindromos validos (DP sobre la primera mitad + unir con el espejo).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int w, D;
int NX[4][3] = {{1, 3, -1}, {0, 2, 3}, {0, 3, -1}, {0, 1, -1}}; // A=0,B1=1,B2=2,C=3
int LET[4] = {0, 1, 1, 2};
ll dp[60][60][4];
void run(int len) {
    memset(dp, 0, sizeof dp);
    dp[1][0][0] = dp[0][1][1] = dp[0][0][3] = 1;
    for (int step = 1; step < len; step++) {
        static ll nx[60][60][4]; memset(nx, 0, sizeof nx);
        for (int a = 0; a <= step; a++) for (int b = 0; a + b <= step; b++) for (int s = 0; s < 4; s++)
            if (dp[a][b][s]) for (int t = 0; t < 3; t++) if (NX[s][t] >= 0) {
                int ns = NX[s][t], l = LET[ns];
                nx[a + (l == 0)][b + (l == 1)][ns] += dp[a][b][s];
            }
        memcpy(dp, nx, sizeof dp);
    }
}
bool ok(int a, int b, int c) { return max(a, max(b, c)) - min(a, min(b, c)) <= D; }
int main() {
    cin >> w >> D;
    run(w); ll total = 0;
    for (int a = 0; a <= w; a++) for (int b = 0; a + b <= w; b++) for (int s = 0; s < 4; s++)
        if (ok(a, b, w - a - b)) total += dp[a][b][s];
    int h = w / 2; run(h); ll pal = 0;
    for (int a = 0; a <= h; a++) for (int b = 0; a + b <= h; b++) for (int s = 0; s < 4; s++) {
        int c = h - a - b; ll v = dp[a][b][s]; if (!v) continue;
        if (w % 2 == 0) { if (s == 1 && ok(2 * a, 2 * b, 2 * c)) pal += v; }
        else for (int mid = 0; mid < 3; mid++)
            if (mid != LET[s] && ok(2 * a + (mid == 0), 2 * b + (mid == 1), 2 * c + (mid == 2))) pal += v;
    }
    cout << total - pal << endl;
}
