# Genera los casos grandes *.9.in (las salidas se validan comparando py y cpp).
import random
random.seed(7)
w = lambda f, s: open(f, "w").write(s)
n = 1000; w("Adaptation.9.in", f"{n} 30 45\n" + " ".join(str(random.randint(0, 119)) for _ in range(n)) + "\n")
N = 200; cells = [(r, c) for r in range(1, N + 1) for c in range(1, N + 1)]; random.shuffle(cells)
w("Chess.9.in", f"{N} 3\nN 1 1\nN 200 200\nR 100 100\n")
w("Luminosity.9.in", "5000\n" + "".join(f"{l} {l + random.randint(0, 10**12)} {random.randint(1, 10**18)}\n" for l in (random.randint(1, 10**18 - 10**12) for _ in range(5000))))
V = 200000; ed = [(i, i % V + 1) for i in range(1, V + 1)]
ed += [(1, random.randint(3, V - 1)) for _ in range(0)]
# abanico: cuerdas desde 1 a todos los vertices -> outerplanar
ed += [(1, k) for k in range(3, V)]
ed += [(random.randint(1, V - 1),) for _ in range(0)]
ed = ed[:400000]
w("Most.9.in", f"{V} {len(ed)}\n" + "".join(f"{a} {b} {random.randint(-10**9, 10**9)}\n" for a, b in ed))
names = ["N" + "".join(random.choice("abcdefghij") for _ in range(4)) for _ in range(60000)]
w("Genealogy.9.in", "100000\n" + "".join(f"{random.choice(names[1:])}, son of {random.choice(names)}\n" for _ in range(100000)))
w("Hidden.9.in", "".join(s + "\n" for s in (lambda seq: [''.join(c for c in seq if c != str(i)) for i in (1, 2, 3)])(''.join(random.choice("123") for _ in range(100000)))))
