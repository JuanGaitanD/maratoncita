# Propagacion con cola: en cada triangulo (padre, hijo izq, hijo der) si se conocen dos valores
# se deduce el tercero. Contradiccion o valor fuera de [-99,99] -> no solution; si queda
# alguna casilla vacia -> ambiguous.
import sys
from collections import deque
d = sys.stdin.read().split()
n = int(d[0])
v, p = [], 1
for i in range(n):
    v.append([None if int(x) == 100 else int(x) for x in d[p:p + i + 1]]); p += i + 1

def tris(i, j):  # triangulos (fila, col del padre) que contienen la casilla (i, j)
    r = []
    if i < n - 1: r.append((i, j))
    if i > 0:
        if j < i: r.append((i - 1, j))
        if j > 0: r.append((i - 1, j - 1))
    return r

q = deque((i, j) for i in range(n - 1) for j in range(i + 1))
bad = False
while q and not bad:
    i, j = q.popleft()
    P, A, B = v[i][j], v[i + 1][j], v[i + 1][j + 1]
    known = (P is not None) + (A is not None) + (B is not None)
    if known == 3:
        if P != A + B: bad = True
        continue
    if known < 2: continue
    if P is None: cell, val = (i, j), A + B
    elif A is None: cell, val = (i + 1, j), P - B
    else: cell, val = (i + 1, j + 1), P - A
    if not -99 <= val <= 99: bad = True; break
    v[cell[0]][cell[1]] = val
    q.extend(tris(*cell))
if bad: print("no solution")
elif any(x is None for row in v for x in row): print("ambiguous")
else: print("solvable\n" + "\n".join(" ".join(map(str, row)) for row in v))
