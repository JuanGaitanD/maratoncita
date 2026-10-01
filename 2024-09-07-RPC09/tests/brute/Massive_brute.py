# Simulacion por unidad de tiempo (pesos pequenos): BFS sobre estados de ambas personas.
import sys
d=sys.stdin.read().split(); n,x,y=int(d[0]),int(d[1]),int(d[2])
L=[]
for i in range(x+y):
    u,v,w=int(d[3+3*i]),int(d[4+3*i]),int(d[5+3*i]); L.append((u,v,w,0 if i<x else 1))
def opts(s):  # s=(pos,comp,rem): comp=-1 idle
    p,c,r=s
    if c>=0: return [(p,c,r-1) if r>1 else (p,-1,0)]
    o=[s]
    for u,v,w,cc in L:
        if u==p: o.append((v,cc,w-1) if w>1 else (v,-1,0))  # salida inmediata con w-1 restantes; comp registrada
    return o
# guardar compania en uso: estado con rem>0 => en uso; para w==1 el uso dura solo este paso
from itertools import product
start=((1,-1,0),(1,-1,0)); cur={start}; t=0
def step(s):
    res=set()
    def moves(st):
        p,c,r=st
        if c>=0: return [(st,c, (p,c,r-1) if r>1 else (p,-1,0))]
        o=[(st,-1,st)]
        for u,v,w,cc in L:
            if u==p: o.append((st,cc,(v,cc,w-1) if w>1 else (v,-1,0)))
        return o
    for (a0,ca,a1),(b0,cb,b1) in product(moves(s[0]),moves(s[1])):
        if ca>=0 and ca==cb: continue
        res.add((a1,b1))
    return res
while True:
    if any(a==(n,-1,0) and b==(n,-1,0) for a,b in cur): print(t); break
    nxt=set()
    for s in cur: nxt|=step(s)
    cur=nxt; t+=1
