// Si n > c apostar c+1 (ganas vaca); si n == c empatar con c; si n < c perder igual: apostar 0.
#include <bits/stdc++.h>
using namespace std;
int main() {
    long long c, n; cin >> c >> n;
    cout << (n > c ? c + 1 : (n == c ? c : 0)) << endl;
}
