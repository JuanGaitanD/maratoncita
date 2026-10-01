// DP sobre los 16 dados: estado = ultima letra puesta; caras: arriba 0, lados 1, abajo 2 giros.
// La cara Q cuenta como "QU": exige previa <= Q y deja como ultima la U.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string r[6];
    for (int k = 0; k < 6; k++) cin >> r[k];
    const int INF = 1e9;
    vector<int> dp(26, INF);
    dp[0] = 0;
    for (int i = 0; i < 16; i++) {
        vector<int> nd(26, INF);
        for (int k = 0; k < 6; k++) {
            int c = r[k][i] - 'A', w = (k == 0 ? 0 : k == 5 ? 2 : 1);
            int nxt = (c == 'Q' - 'A') ? 'U' - 'A' : c;
            for (int l = 0; l <= c; l++)
                if (dp[l] < INF) nd[nxt] = min(nd[nxt], dp[l] + w);
        }
        dp = nd;
    }
    int best = *min_element(dp.begin(), dp.end());
    if (best >= INF) puts("impossible");
    else printf("%d\n", best);
}
