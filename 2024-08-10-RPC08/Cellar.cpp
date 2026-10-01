// Serie (A+B) necesita max(A,B) profesores; paralelo (A*B) necesita A+B; () necesita 1.
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    vector<long long> val(1, 0); vector<char> op(1, 0);  // val 0 = aun vacio
    for (char ch : s) {
        if (ch == '(') { val.push_back(0); op.push_back(0); }
        else if (ch == ')') {
            long long v = val.back(); val.pop_back(); op.pop_back();
            if (v == 0) v = 1;
            if (val.back() == 0) val.back() = v;
            else if (op.back() == '+') val.back() = max(val.back(), v);
            else val.back() += v;
        } else op.back() = ch;
    }
    cout << val[0] << "\n";
}
