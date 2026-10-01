# Comparar c^2 con a^2 + b^2 en enteros: igual -> R, menor -> A (agudo), mayor -> O (obtuso).
import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for k in range(d[0]):
    a, b, c = d[1 + 3 * k:4 + 3 * k]
    s = a * a + b * b
    out.append("R" if c * c == s else ("A" if c * c < s else "O"))
print(" ".join(out))
