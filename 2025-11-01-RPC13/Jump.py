# a = menor/3 y c = mayor/3; se prueba cada b y se compara el conjunto de sumas de 3 saltos con la lista.
from itertools import combinations_with_replacement as cwr
n = int(input())
d = list(map(int, input().split()))
a, c, target = d[0] // 3, d[-1] // 3, set(d)
for b in range(a + 1, c):
    if {sum(t) for t in cwr((a, b, c), 3)} == target:
        print(a, b, c)
        break
