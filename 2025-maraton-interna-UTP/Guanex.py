# Cola de prioridad (min-heap): 1 x inserta, 2 elimina el minimo, 3 consulta el minimo.
import sys, heapq
d = sys.stdin.buffer.read().split()
h, out, p = [], [], 1
for _ in range(int(d[0])):
    op = d[p]; p += 1
    if op == b"1":
        heapq.heappush(h, int(d[p])); p += 1
    elif op == b"2":
        if h:
            heapq.heappop(h)
    else:
        out.append(str(h[0]) if h else "Empty!")
sys.stdout.write("\n".join(out) + ("\n" if out else ""))
