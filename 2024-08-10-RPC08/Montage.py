# Posible si y solo si ninguna altura se repite mas de w veces (w columnas estrictas).
import sys
from collections import Counter
d = sys.stdin.buffer.read().split()
n, w = int(d[0]), int(d[1])
print("yes" if max(Counter(d[2:2 + n]).values()) <= w else "no")
