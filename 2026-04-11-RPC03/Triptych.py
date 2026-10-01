# DP por (cuantas A, cuantas B, estado final: A, B simple, BB, C). Se cuentan las validas y se
# restan los palindromos validos (DP sobre la primera mitad + unir con el espejo).
import sys
w, D = map(int, sys.stdin.read().split())
A, B1, B2, C = range(4)
NXT = {A: [(B1, 1), (C, 2)], B1: [(A, 0), (B2, 1), (C, 2)], B2: [(A, 0), (C, 2)], C: [(A, 0), (B1, 1)]}
LET = [0, 1, 1, 2]  # letra (0=A,1=B,2=C) de cada estado

def run(length):  # dict (a, b, estado) -> cantidad, secuencias validas (regla 1) de largo length
    cur = {(1, 0, A): 1, (0, 1, B1): 1, (0, 0, C): 1}
    for _ in range(length - 1):
        nxt = {}
        for (a, b, s), c in cur.items():
            for ns, l in NXT[s]:
                key = (a + (l == 0), b + (l == 1), ns)
                nxt[key] = nxt.get(key, 0) + c
        cur = nxt
    return cur

ok = lambda a, b, c: max(a, b, c) - min(a, b, c) <= D
total = sum(c for (a, b, s), c in run(w).items() if ok(a, b, w - a - b))
pal, h = 0, w // 2
for (a, b, s), c in run(h).items():
    cc = h - a - b
    if w % 2 == 0:
        if s == B1 and ok(2 * a, 2 * b, 2 * cc): pal += c
    else:
        for mid in range(3):
            if mid != LET[s] and ok(2 * a + (mid == 0), 2 * b + (mid == 1), 2 * cc + (mid == 2)):
                pal += c
print(total - pal)
