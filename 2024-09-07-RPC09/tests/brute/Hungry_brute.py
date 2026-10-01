import sys
d=sys.stdin.read().split(); n,w=int(d[0]),int(d[1]); c=list(map(int,d[2:2+n])); o=[]
for i in range(n):
    cs=[c[j] for j in range(n) if j!=i]+[2*c[i]]; dp=[0]+[10**9]*w
    for x in range(1,w+1):
        for v in cs:
            if v<=x: dp[x]=min(dp[x],dp[x-v]+1)
    o.append("impossible" if dp[w]>=10**9 else str(dp[w]))
print(" ".join(o))
