# Fuerzas brutas para Haggling, Document, Gamer, Beacons y comparacion aleatoria.
import random, subprocess, sys, itertools
from collections import deque
def run(name, inp):
    return subprocess.run([sys.executable, "../../" + name + ".py"], input=inp, capture_output=True, text=True).stdout.strip()
def longest(iv):
    iv = sorted(iv, key=lambda t: t[1]); best = {}
    L = []
    for i, (a, b) in enumerate(iv):
        L.append(1 + max([L[j] for j in range(i) if iv[j][1] + 1 <= a] or [0]))
    return max(L or [0])
def hag(iv):
    k = longest(iv)
    for r in range(1, len(iv) + 1):
        for rem in itertools.combinations(range(len(iv)), r):
            if longest([iv[i] for i in range(len(iv)) if i not in rem]) < k: return r
def doc(ws):
    best = None
    for W in range(max(map(len, ws)), sum(map(len, ws)) + len(ws)):
        lines, cur = 1, -1
        for w in ws:
            if cur + 1 + len(w) <= W: cur += 1 + len(w)
            else: lines += 1; cur = len(w)
        best = W + lines if best is None else min(best, W + lines)
    return best
def gam(tiles):
    tiles = frozenset(tiles)
    melds = []
    for v in range(1, 14):
        for k in (3, 4):
            for cs in itertools.combinations(range(4), k): melds.append(frozenset((c, v) for c in cs))
    for c in range(4):
        for a in range(1, 14):
            for b in range(a + 2, 14): melds.append(frozenset((c, v) for v in range(a, b + 1)))
    melds = [m for m in melds if m <= tiles]
    memo = {}
    def f(s):
        if not s: return True
        if s in memo: return memo[s]
        x = min(s); r = any(x in m and m <= s and f(s - m) for m in melds)
        memo[s] = r; return r
    return f(tiles)
def bea(h):
    r, c = len(h), len(h[0])
    def vis(a, b):
        (y1, x1), (y2, x2) = a, b
        if y1 != y2 and x1 != x2: return False
        D = abs(y1 - y2) + abs(x1 - x2)
        for t in range(1, D):
            y = y1 + (y2 - y1) // D * t; x = x1 + (x2 - x1) // D * t
            if (h[y][x] - h[y1][x1]) * D > (h[y2][x2] - h[y1][x1]) * t: return False
        return True
    dist = {(0, 0): 0}; q = deque([(0, 0)])
    while q:
        u = q.popleft()
        for y in range(r):
            for x in range(c):
                if (y, x) not in dist and (y, x) != u and vis(u, (y, x)):
                    dist[(y, x)] = dist[u] + 1; q.append((y, x))
    return dist[(r - 1, c - 1)] - 1
random.seed(1)
cols = ["Red", "Yellow", "Blue", "Black"]
for it in range(300):
    n = random.randint(1, 7); iv = set()
    while len(iv) < n:
        a = random.randint(0, 12); iv.add((a, a + random.randint(1, 4)))
    iv = list(iv); inp = "%d\n" % n + "".join("%d %d\n" % t for t in iv)
    assert run("Haggling", inp) == str(hag(iv)), inp
    ws = ["x" * random.randint(1, 6) for _ in range(random.randint(1, 12))]
    inp = "%d\n%s\n" % (len(ws), " ".join(ws)); assert run("Document", inp) == str(doc(ws)), inp
    t = set()
    for _ in range(random.randint(1, 12)): t.add((random.randint(0, 3), random.randint(1, 6)))
    inp = "%d\n" % len(t) + "".join("%s %d\n" % (cols[c], v) for c, v in t)
    assert run("Gamer", inp) == ("possible" if gam(t) else "impossible"), inp
    r, c = random.randint(2, 5), random.randint(2, 5)
    h = [[random.randint(0, 9) for _ in range(c)] for _ in range(r)]
    inp = "%d %d\n" % (r, c) + "".join("".join(map(str, row)) + "\n" for row in h)
    assert run("Beacons", inp) == str(bea(h)), inp
print("brute OK")
