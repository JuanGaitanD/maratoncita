import sys
from itertools import permutations
d=sys.stdin.read().split(); n=int(d[0]); sw=[(int(d[2+2*i]),int(d[3+2*i])) for i in range(n)]; b=None
for p in permutations(sw):
    pos=1;t=0
    for c,m in p: t+=c*pos; pos+=m
    b=t if b is None else min(b,t)
print(b)
