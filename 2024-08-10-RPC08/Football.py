# N(k): rutas de longitud k (Fibonacci); E(k) = E(k-1) + E(k-2) + N(k) escalones totales.
import sys
def main():
    d = sys.stdin.buffer.read().split()
    n, q = int(d[0]), int(d[1])
    M = 10**9 + 7
    N = [1] * (n + 1); E = [0] * (n + 1)
    for k in range(2, n + 1):
        N[k] = (N[k - 1] + N[k - 2]) % M
    if n >= 1: E[1] = 1
    for k in range(2, n + 1):
        E[k] = (E[k - 1] + E[k - 2] + N[k]) % M
    out = [str(E[int(d[3 + 2 * i]) - int(d[2 + 2 * i])]) for i in range(q)]
    print("\n".join(out))
main()
