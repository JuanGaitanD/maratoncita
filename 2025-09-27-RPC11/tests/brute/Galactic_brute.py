# Fuerza bruta: alcanzables por barrido hasta LIM con valores pequenos.
import random, subprocess, sys
def brute(s, p, K, LIM=100000):
    R = [False] * (LIM + 1); R[0] = True
    for x in range(LIM + 1):
        if not R[x]: continue
        for a in s:
            if x + a <= LIM: R[x + a] = True
        if any(x % q == 0 for q in p):
            for dl in range(1, K + 1):
                if x + dl <= LIM and any((x + dl) % q == 0 for q in p): R[x + dl] = True
    un = [x for x in range(LIM + 1) if not R[x]]
    if not un: return -1
    if un[-1] > LIM // 2: return -1     # infinitos
    return un[-1]
for it in range(150):
    S, P, K = random.randint(1, 3), random.randint(1, 3), random.randint(1, 10)
    s = [random.randint(1, 12) for _ in range(S)]; p = [random.randint(1, 12) for _ in range(P)]
    inp = f"{S} {P} {K}\n{' '.join(map(str, s))}\n{' '.join(map(str, p))}\n"
    out = subprocess.run([sys.executable, "Galactic.py"], input=inp, capture_output=True, text=True).stdout.strip()
    if int(out) != brute(s, p, K): print("BAD", inp, out, brute(s, p, K)); break
else: print("ok")
