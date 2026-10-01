# DP por longitud t: estado (a = actos leidos del manuscrito 1, b = t - a del 2, manuscrito actual, cambios k).
# El ultimo registro queda determinado por (a, b, actual).
import sys


def main():
    d = sys.stdin.read().split()
    K, T = int(d[0]), int(d[1])
    n1 = int(d[2])
    A = d[3:3 + n1]
    n2 = int(d[3 + n1])
    B = d[4 + n1:4 + n1 + n2]
    NEG = -10 ** 6
    dp = [[[NEG] * (K + 1) for _ in range(2)] for _ in range(T + 2)]
    dp[1][0][0] = 0
    for t in range(1, T):
        nx = [[[NEG] * (K + 1) for _ in range(2)] for _ in range(T + 2)]
        for a in range(t + 1):
            b = t - a
            nA = A[a % n1]
            nB = B[b % n2]
            for c in range(2):
                if (c == 0 and a == 0) or (c == 1 and b == 0):
                    continue
                last = A[(a - 1) % n1] if c == 0 else B[(b - 1) % n2]
                gA = last == nA
                gB = last == nB
                row = dp[a][c]
                for k in range(K + 1):
                    v = row[k]
                    if v < 0:
                        continue
                    k0 = k + (c != 0)
                    k1 = k + (c != 1)
                    if k0 <= K and nx[a + 1][0][k0] < v + gA:
                        nx[a + 1][0][k0] = v + gA
                    if k1 <= K and nx[a][1][k1] < v + gB:
                        nx[a][1][k1] = v + gB
        dp = nx
    best = 0
    for a in range(T + 2):
        for c in range(2):
            best = max(best, max(dp[a][c]))
    print(best)


main()
