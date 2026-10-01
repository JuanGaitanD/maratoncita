# Genera tests de ejemplo (del enunciado) y casos extra (.9) con fuerzas brutas.
import os, random, itertools, functools, sys
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def w(name, i, inp, out):
    open(os.path.join(T, "%s.%d.in" % (name, i)), "w", newline="\n").write(inp.strip() + "\n")
    open(os.path.join(T, "%s.%d.out" % (name, i)), "w", newline="\n").write(out.strip() + "\n")
S = {
 "Peasy": [("10 20", "E"), ("6 13", "H"), ("15 22", "E")],
 "Age": [("69 9 1", "1"), ("76 11 7", "1"), ("50 9 3", "0"), ("70 10 5", "1"), ("10 7 2", "0")],
 "Increasing": [("6\n5 7 2 4 6 3", "3"), ("15\n10 70 80 5 5 5 15 20 30 40 60 9 8 70 80", "6")],
 "Portmanteau": [("abcdefun\nghijku", "abcdijku"), ("abcdefun\nghmn", "abcdeghmn"), ("abycd\nfgyhu", "abycdofgyhu")],
 "Weighted": [("6 3\n3\n6\n2\n3\n5\n4", "2 19\n1 21\n3 23\n4 25"), ("7 3\n2\n3\n2\n3\n2\n4\n1", "5 13\n1 14\n3 14\n2 16\n4 19")],
 "Triangles": [("2\n1 1\n2 1\n2 2\n4 2\n4 3\n5 3", "0.0"), ("3\n3 3\n2 5\n9 3\n3 2\n2 1\n7 2\n10 8\n10 6\n1 10", "1.0")],
 "Rightsizing": [("5 6\neduardo 6000000\nmark 7000000\nandrew 5000000\ndustin 1000000\nchris 500000\n2\n1 andrew 2000000\n1 dustin 5000000\n2\n2\n2",
                  "mark 7000000\nandrew 7000000\ndustin 6000000\neduardo 6000000"),
                 ("10 15\na 6\nb 5\nc 4\nd 2\ne 1\nf 3\ng 8\nh 10\ni 7\nj 10\n1 c 4\n1 d 9\n2\n1 e 3\n1 h 1\n1 b 6\n2\n2\n1 f 6\n1 a 3\n2\n1 i 2\n2\n1 e 5\n2",
                  "d 11\nb 11\nh 11\nj 10\na 9\ne 9")],
 "Brightline": [("5 8\n1 2 b 7\n1 3 b 3\n3 2 b 4\n2 4 r 2\n3 5 r 5\n5 2 b 1\n4 3 b 6\n5 4 b 4", "2\n4\n5"),
                ("5 9\n1 2 b 3\n1 5 r 4\n1 3 b 8\n2 4 b 1\n2 5 b 7\n3 2 b 4\n4 1 b 2\n4 3 r 5\n5 4 b 6", "3\n5")],
 "ABC": [("2 3 1", "10"), ("15 2 7", "0")],
 "Cake": [("4\n6 4\n3 4\n4 5\n5 5", "1.0"), ("5\n10 10\n8 15\n13 16\n18 15\n16 10", "15.0")],
}
for name, cases in S.items():
    for i, (a, b) in enumerate(cases, 1):
        w(name, i, a, b)
random.seed(7)
# ABC: DP brute sobre (a, b, c, ultima)
@functools.lru_cache(None)
def abc(x, y, z, last):
    if x + y + z == 0: return 1
    r = 0
    for k, v in enumerate((x, y, z)):
        if v and k != last:
            t = [x, y, z]; t[k] -= 1; r += abc(t[0], t[1], t[2], k)
    return r
w("ABC", 8, "4 5 3", str(abc(4, 5, 3, -1) % (10**9 + 7)))
sys.setrecursionlimit(10000)
w("ABC", 9, "40 37 30", str(abc(40, 37, 30, -1) % (10**9 + 7)))
# Age: brute doble
w("Age", 9, "150 149 1", str(int(any(a*149+k*1 == 150 for a in range(1, 2) for k in range(1, 151)))))
# Weighted: n grande (salida por brute O(nk) con k chico)
n, k = 2000, 50
v = [random.randint(1, 10**8) for _ in range(n)]
res = sorted((sum((j+1)*v[i+j] for j in range(k)), i+1) for i in range(n-k+1))
w("Weighted", 9, "%d %d\n" % (n, k) + "\n".join(map(str, v)), "\n".join("%d %d" % (i, s) for s, i in res))
# Cake: hexagono convexo horario, brute por fuerza
P = [(1, 1), (1, 500), (300, 999), (999, 700), (900, 200), (400, 2)][::-1]
P = P[::-1]  # orden horario no importa para |area|
def ar2(pts): return abs(sum(pts[i][0]*pts[i-1][1]-pts[i-1][0]*pts[i][1] for i in range(len(pts))))
Sx = ar2(P); best = min(abs(Sx - 2*ar2(P[i:j+1])) for i in range(6) for j in range(i+2, 6) if (i, j) != (0, 5))
w("Cake", 9, "6\n" + "\n".join("%d %d" % p for p in P), "%d.%d" % (best//2, 5*(best % 2)))
# Triangles: n=3 aleatorio, brute por permutaciones
pts = random.sample([(x, y) for x in range(1, 40) for y in range(1, 40)], 9)
def a3(p, q, r): return abs((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
bt = min(max(a3(*[pts[i] for i in pm[t:t+3]]) for t in (0, 3, 6)) - min(a3(*[pts[i] for i in pm[t:t+3]]) for t in (0, 3, 6)) for pm in itertools.permutations(range(9)))
w("Triangles", 9, "3\n" + "\n".join("%d %d" % p for p in pts), "%d.%d" % (bt//2, 5*(bt % 2)))
# Rightsizing: simulacion lineal
names = ["e%s" % chr(97+i) for i in range(8)]; sal = {e: random.randint(1, 5) for e in names}
acts = []; out = []; alive = dict(sal)
for _ in range(20):
    if alive and random.random() < 0.35:
        mx = max(alive.values()); e = min(x for x in alive if alive[x] == mx); out.append("%s %d" % (e, mx)); del alive[e]; acts.append("2")
    elif alive:
        e = random.choice(sorted(alive)); r = random.randint(1, 3); alive[e] += r; acts.append("1 %s %d" % (e, r))
w("Rightsizing", 9, "8 %d\n" % len(acts) + "\n".join("%s %d" % (e, sal[e]) for e in names) + "\n" + "\n".join(acts), "\n".join(out))
# Brightline: DAG aleatorio, brute Bellman-Ford clasico
n, edges = 30, []
for _ in range(80):
    s, e = random.sample(range(1, n+1), 2)
    if s > e: s, e = e, s
    edges.append((s, e, random.choice("br"), random.randint(1, 20)))
D = [float("inf")]*(n+1); D[1] = 0
for _ in range(n):
    for s, e, t, a in edges:
        c = -a if t == "r" else a
        if D[s] + c < D[e]: D[e] = D[s] + c
w("Brightline", 9, "%d %d\n" % (n, len(edges)) + "\n".join("%d %d %s %d" % x for x in edges), "\n".join(str(v) for v in range(1, n+1) if D[v] < 0))
w("Peasy", 9, "0 1", "H")
w("Increasing", 9, "1\n5", "1")
w("Portmanteau", 9, "bcdf\nghjk", "bcdfoghjk")
