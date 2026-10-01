# Beauquier-Nivat: B = X Y Xb Yb o X Y Z Xb Yb Zb (Xb = reverso complementado), h = k/2.
# Arco bueno (q, L): B[q..q+L) y B[q+h..q+h+L) son reverso-complemento. Con centro fijo los
# arcos buenos estan anidados: se expanden desde cada centro. Luego se cuentan cadenas de 2 y 3
# arcos que suman h con bitsets (enteros). Cada una aparece 2 veces (s y s+h) en las rotaciones.
import sys
d = sys.stdin.read().split()
k, s = int(d[0]), d[1]
comp = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
if k % 2: print(0); sys.exit()
h = k // 2
cs = [comp[c] for c in s]
out = [0] * h   # out[q]: bit L si el arco (q, L) es bueno
rin = [0] * h   # rin[e]: bit h-L si hay arco bueno de largo L que termina en e
for c2 in range(k):  # c2 = l + r (extremos inclusivos)
    S = c2 + h
    if c2 % 2 == 0: l = r = c2 // 2
    else: l, r = c2 // 2, c2 // 2 + 1
    ok = cs[l % k] == s[(S - l) % k] and (l == r or cs[r % k] == s[(S - r) % k])
    while ok and r - l + 1 < h:
        L = r - l + 1; q = l % h
        out[q] |= 1 << L; rin[(q + L) % h] |= 1 << (h - L)
        l -= 1; r += 1
        ok = cs[l % k] == s[(S - l) % k] and cs[r % k] == s[(S - r) % k]
pc = getattr(int, "bit_count", None) or (lambda x: bin(x).count("1"))
tot = 0
for q1 in range(h):
    o, R = out[q1], rin[q1]
    while o:
        low = o & -o; a = low.bit_length() - 1; o ^= low
        o2 = out[(q1 + a) % h]
        tot += ((o2 >> (h - a)) & 1) + pc(o2 & (R >> a))
print(2 * tot)
