# a[n] = cadenas de largo n sin S, b[n] = cadenas cuya primera aparicion de S termina en n.
# K*a[n-1] = a[n] + b[n]  y  a[n-m] = sum_{j borde de S} b[n-m+j]  (Guibas-Odlyzko).
# Respuesta: K^N - a[N].  O(N * #bordes).
import sys
MOD = 10**9 + 7
def main():
    t = sys.stdin.read().split()
    N, K, S = int(t[0]), int(t[1]), t[2]
    m = len(S)
    J = [j for j in range(1, m) if S[:j] == S[m - j:]]   # bordes propios
    a = [0] * (N + 1); b = [0] * (N + 1)
    a[0] = 1
    for n in range(1, N + 1):
        if n < m:
            a[n] = a[n - 1] * K % MOD
            continue
        o = n - m
        x = (a[o] - sum([b[o + j] for j in J])) % MOD
        b[n] = x
        a[n] = (a[n - 1] * K - x) % MOD
    print((pow(K, N, MOD) - a[N]) % MOD)
main()
