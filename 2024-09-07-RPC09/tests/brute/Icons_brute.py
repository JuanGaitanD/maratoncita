import sys
from itertools import permutations
d=sys.stdin.read().split(); N=int(d[0]); s=list(map(int,d[1:]))
best=min((max(p[:N])+max(p[N:]))*sum(max(p[i],p[N+i]) for i in range(N)) for p in permutations(s))
print(best)
