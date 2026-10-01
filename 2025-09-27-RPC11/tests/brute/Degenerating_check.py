# Compara Degenerating.py contra Degenerating_brute.py (O(n^2)) en arboles aleatorios.
import random, subprocess, sys
for it in range(400):
    n = random.randint(1, 12); k = random.randint(1, 6); m = random.randint(1, k)
    tgt = random.sample(range(1, k + 1), m); val = [random.randint(1, k) for _ in range(n)]
    q = random.randint(2, 50); p = random.randint(1, q - 1)
    ed = [(random.randint(1, i - 1), i) for i in range(2, n + 1)]
    perm = list(range(1, n + 1)); random.shuffle(perm)
    inp = f"{n} {m} {k} {p} {q}\n{' '.join(map(str, tgt))}\n{' '.join(map(str, val))}\n" + "".join(f"{perm[a-1]} {perm[b-1]}\n" for a, b in ed)
    a = subprocess.run([sys.executable, "Degenerating.py"], input=inp, capture_output=True, text=True)
    b = subprocess.run([sys.executable, "tests/brute/Degenerating_brute.py"], input=inp, capture_output=True, text=True)
    if a.stdout != b.stdout: print("BAD", inp, a.stdout, a.stderr, b.stdout); break
else: print("ok")
