# Genera casos .9 grandes (estres); las salidas se calculan con la solucion y se cruzan con C++.
import random
random.seed(7)
def w(name, s): open(name + ".9.in", "w").write(s)
w("Athletes", "Zyxwwvutsrqponmlkjihgfedcbaa\n")
w("Beacons", "100 100\n" + "".join("".join(str(random.randint(0, 9)) for _ in range(100)) + "\n" for _ in range(100)))
# serie de 1 con paralelo profundo: ((...((()*())*())...)
k = 249990; w("Cellar", "(" * k + "()" + "*())" * (k - 1) + "+())" + "\n")
ws = ["a" * random.randint(1, 3) for _ in range(400000)]; w("Document", "%d\n%s\n" % (len(ws), " ".join(ws)))
w("Euroexpress", "200000\n" + "".join("%d %d\n" % (random.randint(1, 10**6), random.randint(1, 10**6)) for _ in range(200000)))
w("Football", "1000000 50000\n" + "".join("%d %d\n" % tuple(sorted((random.randint(1, 10**6), random.randint(1, 10**6)))) for _ in range(50000)))
w("Gamer", "52\n" + "".join("%s %d\n" % (c, v) for c in ["Red", "Yellow", "Blue", "Black"] for v in range(1, 14)))
iv = set()
while len(iv) < 1000:
    a = random.randint(0, 3000); iv.add((a, a + random.randint(1, 30)))
w("Haggling", "1000\n" + "".join("%d %d\n" % t for t in iv))
w("Identity", "0.001 5.000\n")
pts = [(5 * 10**8, 5 * 10**8 + i) for i in range(50000)] + [(5 * 10**8 + 1, 5 * 10**8 + 49999 - i) for i in range(50000)]
w("Jog", "0 1000000000 100000\n" + "".join("%d %d\n" % p for p in pts))
w("Keys", "AB Ba  b" * 125 + "\n")
w("Longbottom", "1" + "0" * 999998 + "1\n")
w("Montage", "200000 2\n" + " ".join(str(i // 2) for i in range(200000)) + "\n")
