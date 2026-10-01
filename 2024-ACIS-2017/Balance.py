# Fuerza bruta sobre (i, j, k) copias de cada pesa: la balanza queda equilibrada si todas
# van al otro platillo o si una sola clase acompana al objeto. O(C^3), C pequeno.
import sys
c, w, t1, t2, t3 = map(int, sys.stdin.read().split())
r = 0
for i in range(c + 1):
    for j in range(c + 1):
        for k in range(c + 1):
            a, b, d = i * t1, j * t2, k * t3
            if a + b + d == w or w + a == b + d or w + b == a + d or w + d == a + b:
                r += 1
print(r)
