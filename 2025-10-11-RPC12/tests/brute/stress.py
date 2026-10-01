# Fuerza bruta + generadores aleatorios para A, G, L, M. Uso: python stress.py
import random, subprocess, sys, itertools, os
D = os.path.dirname(os.path.abspath(__file__)) + "/../../"
def run(name, inp):
    return subprocess.run([sys.executable, D + name + ".py"], input=inp, capture_output=True, text=True).stdout.strip()

def bA(n, l, h, a):
    best = -1
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i + 1 for i in range(n - 1) if mask >> i & 1] + [n]
        ok = all(any(all(l <= a[j] + 12 * k <= h for j in range(cuts[s], cuts[s + 1])) for k in range(-12, 13)) for s in range(len(cuts) - 1))
        if ok: best = max(best, min(cuts[s + 1] - cuts[s] for s in range(len(cuts) - 1)))
    return best

def bL(rs):
    req = {}
    for l, r, t in rs:
        for x in range(l, r + 1): req[x] = max(req.get(x, 0), t)
    best = None
    for perm in itertools.permutations(req):
        p = tm = 0
        for x in perm: tm = max(tm + abs(x - p), req[x]); p = x
        best = tm if best is None else min(best, tm)
    return best

def bM(V, edges):
    best = None
    adj = [[] for _ in range(V + 1)]
    for i, (a, b, s) in enumerate(edges): adj[a].append((b, s, i)); adj[b].append((a, s, i))
    def dfs(st, v, used, vis, w, cnt):
        nonlocal best
        for u, s, i in adj[v]:
            if i in used: continue
            if u == st and cnt >= 1:
                best = w + s if best is None else max(best, w + s)
            elif u not in vis and u > st:
                dfs(st, u, used | {i}, vis | {u}, w + s, cnt + 1)
    for st in range(1, V + 1): dfs(st, st, frozenset(), {st}, 0, 0)
    return best

def genM():
    k = random.randint(2, 4)
    V = k; edges = [(i + 1, i % k + 2 if i + 1 < k else 1) for i in range(k)]
    if k == 2: edges = [(1, 2), (1, 2)]
    outer = list(range(len(edges)))
    for _ in range(random.randint(0, 3)):
        ei = random.choice(outer); outer.remove(ei)
        u, v = edges[ei]; m = random.randint(0, 2)
        path = [u] + list(range(V + 1, V + 1 + m)) + [v]; V += m
        for a, b in zip(path, path[1:]): edges.append((a, b)); outer.append(len(edges) - 1)
    return V, [(a, b, random.randint(-5, 5)) for a, b in edges]

def bG(lines):
    n = len(lines)
    names = set(a for a, b in lines) | set(b for a, b in lines)
    for R in names:
        opts = [[j for j in range(n) if j != i and lines[j][0] == lines[i][1]] + ([-1] if lines[i][1] == R else []) for i in range(n)]
        for ch in itertools.product(*opts):
            ok = True
            for i in range(n):
                v, seen = i, set()
                while v != -1 and v not in seen: seen.add(v); v = ch[v]
                if v != -1: ok = False; break
            if ok: return "possible"
    return "impossible"

random.seed(1)
for it in range(300):
    n = random.randint(1, 9); l = random.randint(0, 20); h = l + 11 + random.randint(0, 6)
    a = [random.randint(0, 50) for _ in range(n)]
    inp = f"{n} {l} {h}\n{' '.join(map(str, a))}\n"
    assert run("Adaptation", inp) == str(bA(n, l, h, a)), inp
    rs = []
    for _ in range(random.randint(1, 3)):
        l = random.randint(1, 6); r = min(l + random.randint(0, 2), 7); rs.append((l, r, random.randint(1, 15)))
    inp = f"{len(rs)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in rs)
    assert run("Luminosity", inp) == str(bL(rs)), inp
    V, ed = genM()
    inp = f"{V} {len(ed)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in ed)
    assert run("Most", inp) == str(bM(V, ed)), inp
    nm = ["Aa", "Bb", "Cc"]
    ls = [(random.choice(nm), random.choice(nm)) for _ in range(random.randint(1, 4))]
    inp = f"{len(ls)}\n" + "".join(f"{a}, son of {b}\n" for a, b in ls)
    assert run("Genealogy", inp) == bG(ls), inp
print("stress OK")
