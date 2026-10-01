# Burbuja: en cada pasada el mayor restante "sube" al final. O(n^2).
import sys
d = list(map(int, sys.stdin.read().split()))
n, a = d[0], d[1:1 + d[0]]
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(" ".join(map(str, a)))
