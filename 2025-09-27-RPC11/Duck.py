# Con n = total/3 equipos, se puede repartir sii ningun color tiene mas de n patos.
import sys
a = list(map(int, sys.stdin.read().split()))
d = a[1:a[0] + 1]
print("YES" if 3 * max(d) <= sum(d) else "NO")
