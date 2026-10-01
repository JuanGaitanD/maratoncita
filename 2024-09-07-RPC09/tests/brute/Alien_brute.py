import sys
d=sys.stdin.read().split(); n,m=int(d[0]),int(d[1])
adj=[set() for _ in range(n+1)]
for i in range(m):
    u,v=int(d[2+2*i]),int(d[3+2*i]); adj[u].add(v); adj[v].add(u)
alive=set(range(1,n+1)); days=0
while True:
    c=[v for v in alive if v!=1]
    days+=1
    if not c: break
    v=max(c,key=lambda x:(len(adj[x]&alive),-x)); alive.discard(v)
    seen={1}; s=[1]
    while s:
        u=s.pop()
        for w in adj[u]&alive:
            if w not in seen: seen.add(w); s.append(w)
    alive=seen
print(days)
