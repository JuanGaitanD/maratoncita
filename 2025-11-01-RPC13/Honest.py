# Contar apariciones de cada numero y listar los que superan 2n.
import sys
data = sys.stdin.buffer.read().split()
n = int(data[0])
cnt = [0] * 51
for x in data[1:]:
    cnt[int(x)] += 1
res = [str(v) for v in range(1, 51) if cnt[v] > 2 * n]
print(" ".join(res) if res else -1)
