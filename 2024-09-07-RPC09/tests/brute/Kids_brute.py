# simulacion Monte Carlo exacta por enumeracion: estados (progreso) con recursion sobre ninos
import sys
d=sys.stdin.read().split(); n,k=int(d[0]),int(d[1]); a=[float(x) for x in d[2:2+k]]
best=0
for g in range(n):
    # prob de que el nino g sea el primero
    def f(kid,prog):
        if kid==g:
            p=1
            for i in range(prog,k): p*=a[i]
            return p
        tot=0; p=1
        for i in range(prog,k):
            tot+=p*(1-a[i])*f(kid+1,i); p*=a[i]
        return tot
    best=max(best,f(0,0))
print("%.10f"%best)
