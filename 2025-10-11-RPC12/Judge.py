# Marca los dias de vacaciones de cada juez y cuenta dias con >= 3 jueces libres. O(n*m).
import sys
def main():
    t = list(map(int, sys.stdin.read().split()))
    n, m = t[0], t[1]
    free = [n] * (m + 1)
    k = 2
    for _ in range(n):
        v = t[k]; k += 1
        for _ in range(v):
            s, e = t[k], t[k + 1]; k += 2
            for d in range(s, e + 1): free[d] -= 1
    print(sum(1 for d in range(1, m + 1) if free[d] >= 3))
main()
