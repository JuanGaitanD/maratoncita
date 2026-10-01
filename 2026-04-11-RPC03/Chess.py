# Backtracking probando capturas en orden lexicografico (origen, destino); la primera
# secuencia completa encontrada es la pedida. Se memorizan los estados sin solucion.
import sys
d = sys.stdin.read().split()
n, m = int(d[0]), int(d[1])
board = {}
for i in range(m):
    loc = d[3 + 2 * i]
    board[(ord(loc[0]) - 65, int(loc[1]) - 1)] = d[2 + 2 * i]
name = lambda c: chr(65 + c[0]) + str(c[1] + 1)
DIAG = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ORTH = [(1, 0), (-1, 0), (0, 1), (0, -1)]
KN = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

def captures(b, c):
    p, out = b[c], []
    if p in 'NK':
        for dr, dc in (KN if p == 'N' else DIAG + ORTH):
            t = (c[0] + dr, c[1] + dc)
            if t in b: out.append(t)
    else:
        dirs = DIAG if p == 'B' else ORTH if p == 'R' else DIAG + ORTH
        for dr, dc in dirs:
            r, k = c[0] + dr, c[1] + dc
            while 0 <= r < n and 0 <= k < n:
                if (r, k) in b: out.append((r, k)); break
                r += dr; k += dc
    return out

dead = set()
def solve(b, path):
    if len(b) == 1: return True
    key = frozenset(b.items())
    if key in dead: return False
    moves = sorted((name(c), name(t), c, t) for c in b for t in captures(b, c))
    for s1, s2, c, t in moves:
        nb = dict(b); nb[t] = nb.pop(c)
        path.append("%s: %s -> %s" % (b[c], s1, s2))
        if solve(nb, path): return True
        path.pop()
    dead.add(key)
    return False

path = []
print("\n".join(path) if solve(board, path) else "No solution")
