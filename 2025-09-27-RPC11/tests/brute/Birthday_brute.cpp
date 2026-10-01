// Fuerza bruta: n * sum_{k<=n} 1/k mod p sumando directamente (n < p).
#include <bits/stdc++.h>
typedef unsigned long long u; const u P=1000000007;
u pw(u b,u e){u r=1;b%=P;while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return r;}
int main(){u n;std::cin>>n;u num=0,den=1;for(u k=1;k<=n;k++){num=(num*k+den)%P;den=den*k%P;}
 std::cout<<n%P*(num*pw(den,P-2)%P)%P<<"\n";}
