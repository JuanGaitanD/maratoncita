// Basta que la cara mayor (q,r) quepa en una restriccion (a<=b); entonces p=q=a, r=b.
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; scanf("%d", &n); long long best = 0;
    for (int i = 0; i < n; i++) {
        long long a, b; scanf("%lld %lld", &a, &b);
        if (a > b) swap(a, b);
        best = max(best, a * a * b);
    }
    printf("%lld\n", best);
}
