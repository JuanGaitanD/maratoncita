d=open(0).read().split(); n,m=int(d[0]),int(d[1]); a=list(map(int,d[2:]))
print(max(a[j]-a[i] for i in range(n) for j in range(i,min(n,i+m+1))))
