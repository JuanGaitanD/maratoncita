# Fuerza bruta recursiva (sin memo) sobre el orden de compra, para conteos pequenos.
import random, subprocess, sys
def rec(L, H, cost, cnt, s):
    if s >= L: return 1.0 if s <= H else 0.0
    tot = sum(cnt)
    if tot == 0: return 0.0
    r = 0.0
    for t in range(3):
        if cnt[t]:
            cnt[t] -= 1; r += (cnt[t] + 1) / tot * rec(L, H, cost, cnt, s + cost[t]); cnt[t] += 1
    return r
for _ in range(200):
    cost = sorted(random.sample(range(1, 30), 3)); cnt = [random.randint(1, 3) for _ in range(3)]
    L = random.randint(1, 80); H = random.randint(L, 100)
    inp = f"{L} {H}\n{' '.join(map(str, cost))}\n{' '.join(map(str, cnt))}\n"
    out = float(subprocess.run([sys.executable, "Weekend.py"], input=inp, capture_output=True, text=True).stdout)
    if abs(out - rec(L, H, cost, cnt, 0)) > 1e-9: print("BAD", inp); break
else: print("ok")
