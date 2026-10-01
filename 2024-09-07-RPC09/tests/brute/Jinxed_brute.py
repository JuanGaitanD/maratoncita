# BFS sobre multiconjuntos de cadenas: abrir un eslabon y unir/abrir; estado = (piezas ordenadas, eslabones abiertos sueltos)
import sys
from functools import lru_cache
d=sys.stdin.read().split(); t=int(d[0]); p=1; o=[]
for _ in range(t):
    n=int(d[p]); a=tuple(sorted(map(int,d[p+1:p+1+n]))); p+=1+n
    # opcion: elegir cuantos eslabones x quitar de los extremos (cualquier distribucion), quedan q piezas, se necesita x>=q
    best=None
    def rec(i,x,q):
        global best
        if i==n:
            if q>=1 and x>=q and (best is None or x<best): best=x
            if q==0: pass
            return
        for take in range(a[i]+1):
            rec(i+1,x+take,q+(1 if take<a[i] else 0))
    rec(0,0,0); o.append(str(best))
print("\n".join(o))
