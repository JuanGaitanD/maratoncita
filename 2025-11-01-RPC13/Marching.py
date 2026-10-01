# Cada paso fija m mod (n-i) = posicion de la letra en la lista restante.
# CRT incremental con modulos no coprimos: se prueba t en a + M*t (k <= 20 intentos).
from math import gcd
n = int(input())
s = input().strip()
rest = [chr(65 + i) for i in range(n)]
a, M, ok = 0, 1, True
for ch in s:
    k, r = len(rest), rest.index(ch)
    rest.pop(r)
    t = next((t for t in range(k) if (a + M * t) % k == r), None)
    if t is None:
        ok = False
        break
    a += M * t
    M = M // gcd(M, k) * k
print("YES\n%d" % a if ok else "NO")
