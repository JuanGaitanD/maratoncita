# dist[j] = prob. de que nadie haya ganado y el progreso global sea j. Cada nino:
# acc(i) = acc(i-1)*a_i + dist[i]; gana con acc(k); nuevo dist[i] = acc(i)*(1-a_{i+1}).
import sys
d = sys.stdin.buffer.read().split()
n, k = int(d[0]), int(d[1]); a = [float(x) for x in d[2:2 + k]]
dist = [0.0] * k; dist[0] = 1.0; best = 0.0
for _ in range(n):
    acc = 0.0; nd = [0.0] * k
    for i in range(k):
        acc += dist[i]
        nd[i] = acc * (1 - a[i])
        acc *= a[i]
    best = max(best, acc); dist = nd
print("%.10f" % best)
