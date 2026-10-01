# Dijkstra sobre estados (calle dirigida actual, largo del tramo continuo acumulado).
# Un par continuo suma al tramo (debe quedar <= d); un par no continuo reinicia el tramo.
import sys, heapq
d = sys.stdin.read().split()
n, m, k, D, s, t = map(int, d[:6])
adj = [[] for _ in range(n + 1)]
L = {}
p = 6
for _ in range(m):
    a, b, l = int(d[p]), int(d[p + 1]), int(d[p + 2]); p += 3
    adj[a].append(b); adj[b].append(a); L[(a, b)] = L[(b, a)] = l
cont = {}
for _ in range(k):
    a, b, c = int(d[p]), int(d[p + 1]), int(d[p + 2]); p += 3
    cont.setdefault((a, b), set()).add(c)
cap = lambda x: min(x, D + 1)
dist = {}
pq = []
for x in adj[s]:
    st = (s, x, cap(L[(s, x)]))
    if dist.get(st, 1 << 60) > L[(s, x)]:
        dist[st] = L[(s, x)]; heapq.heappush(pq, (L[(s, x)], st))
expanded = set()  # aristas ya relajadas por transiciones no continuas
ans = "impossible"
while pq:
    du, st = heapq.heappop(pq)
    if du > dist[st]: continue
    a, b, c = st
    if b == t: ans = du; break
    cs = cont.get((a, b), ())
    first = (a, b) not in expanded
    expanded.add((a, b))
    for x in adj[b]:
        if x == a: continue
        l = L[(b, x)]
        if x in cs:
            if c + l > D: continue
            ns = (b, x, c + l)
        elif first:
            ns = (b, x, cap(l))
        else: continue
        if du + l < dist.get(ns, 1 << 60):
            dist[ns] = du + l; heapq.heappush(pq, (du + l, ns))
print(ans)
