import sys, itertools, random
# genera arbol aleatorio, imprime entrada y la respuesta por fuerza bruta (stderr no usado)
random.seed(int(sys.argv[1])); n = 4; t = random.choice('AO')
levels = [[3]]; 
for lv in range(1, n):
    cnt = sum(e for e in levels[-1] if isinstance(e, int)); row = []
    for _ in range(cnt):
        row.append(random.choice('TF') if lv == n - 1 or random.random() < 0.4 else random.randint(1, 3))
    levels.append(row)
inp = "%d %s\n" % (n, t) + "\n".join(" ".join(map(str, r)) for r in levels) + "\n"
leaves = [(i, j) for i, r in enumerate(levels) for j, e in enumerate(r) if e in ('T', 'F')]
def ev(L):
    below = []
    for lv in range(n - 1, -1, -1):
        isand = (t == 'A') == (lv % 2 == 0); cur = []; k = 0
        for e in L[lv]:
            if e in ('T', 'F'): cur.append(e == 'T')
            else: ch = below[k:k+e]; k += e; cur.append(all(ch) if isand else any(ch))
        below = cur
    return below[0]
base = ev(levels); best = None
for mask in range(1, 1 << len(leaves)):
    L = [list(r) for r in levels]
    for b, (i, j) in enumerate(leaves):
        if mask >> b & 1: L[i][j] = 'F' if L[i][j] == 'T' else 'T'
    if ev(L) != base:
        c = bin(mask).count('1'); best = c if best is None else min(best, c)
open(sys.argv[2] + '.in', 'w').write(inp); open(sys.argv[2] + '.out', 'w').write("%d\n" % best)
