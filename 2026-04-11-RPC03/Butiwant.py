# Mejor caso: todos los votos de cada eliminado (el menor en cada ronda) pasan al segundo.
import sys
d = sys.stdin.read().split()
c = int(d[0]); v = sorted(map(int, d[1:1 + c]))
total = sum(v)
if 2 * v[-1] > total or c == 2:
    print("IMPOSSIBLE TO WIN")
else:
    me, rounds, ans = v[-2], 0, None
    for x in v[:-2]:
        me += x; rounds += 1
        if 2 * me > total:
            ans = rounds; break
    print(ans if ans is not None else "IMPOSSIBLE TO WIN")
