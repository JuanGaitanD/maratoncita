# DP por valor 1..13; estado = largo de la escalera abierta por color (0,1,2,3+).
# Cada ficha va a escalera o al grupo del valor; el grupo debe tener 0, 3 o 4 fichas.
import sys
from itertools import product
def main():
    d = sys.stdin.read().split()
    n = int(d[0]); col = {"Red": 0, "Yellow": 1, "Blue": 2, "Black": 3}
    have = [[False] * 4 for _ in range(14)]
    for i in range(n):
        have[int(d[2 + 2 * i])][col[d[1 + 2 * i]]] = True
    states = {(0, 0, 0, 0)}
    for v in range(1, 14):
        nxt = set()
        for st in states:
            opts = []  # por color: lista de (nuevo_estado, va_al_grupo)
            for c in range(4):
                p = st[c]; o = []
                if have[v][c]:
                    o.append((min(p + 1, 3), 0))
                    if p in (0, 3): o.append((0, 1))
                elif p in (0, 3):
                    o.append((0, 0))
                opts.append(o)
            for ch in product(*opts):
                g = sum(x[1] for x in ch)
                if g in (0, 3, 4):
                    nxt.add(tuple(x[0] for x in ch))
        states = nxt
    ok = any(all(x in (0, 3) for x in st) for st in states)
    print("possible" if ok else "impossible")
main()
