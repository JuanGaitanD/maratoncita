import sys
from itertools import product
d=sys.stdin.read().split(); n,k=int(d[0]),int(d[1]); t=list(map(int,d[2:2+n])); s=list(map(int,d[2+n:]))
best=0
def rec(c,pos,w):
    global best
    if c==k: best=max(best,pos); return
    for r in range(w,n-pos+1):
        if sum(t[pos:pos+r])<=s[c]: rec(c+1,pos+r,r)
rec(0,0,0); print(best)
