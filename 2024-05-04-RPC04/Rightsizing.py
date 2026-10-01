# Max-heap con borrado perezoso de (-salario, nombre); cada aumento inserta una entrada nueva
# y al despedir se descartan las entradas obsoletas (salario distinto o ya despedido).
import sys, heapq
d = sys.stdin.buffer.read().split()
n, a = int(d[0]), int(d[1]); p = 2
sal = {}; h = []
for _ in range(n):
    e = d[p].decode(); s = int(d[p + 1]); p += 2
    sal[e] = s; h.append((-s, e))
heapq.heapify(h)
out = []
for _ in range(a):
    if d[p] == b"1":
        e = d[p + 1].decode(); sal[e] += int(d[p + 2]); p += 3
        heapq.heappush(h, (-sal[e], e))
    else:
        p += 1
        while True:
            s, e = heapq.heappop(h)
            if sal.get(e) == -s:
                break
        del sal[e]
        out.append("%s %d" % (e, -s))
if out:
    sys.stdout.write("\n".join(out) + "\n")
