# Cada punto x (coordenada l_i o r_i) debe atenderse por ultima vez en tiempo >= R(x)=max t que lo cubre.
# Basta con esas coordenadas; los pendientes forman un intervalo y se atiende un extremo:
# DP O(K^2) por longitud del intervalo pendiente. Punto virtual 0 = entrada.
import sys, heapq
def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n = d[0]
    rg = sorted((d[1 + 3 * i], d[2 + 3 * i], d[3 + 3 * i]) for i in range(n))
    xs = sorted(set(d[1::3][:n]) | set(d[2::3][:n]))
    req, h, k = [], [], 0
    for c in xs:
        while k < n and rg[k][0] <= c:
            heapq.heappush(h, (-rg[k][2], rg[k][1])); k += 1
        while h[0][1] < c: heapq.heappop(h)
        req.append(-h[0][0])
    INF = 4 * 10**18
    K = len(xs) + 1
    x = [0] + xs + [0]; t = [0] + req + [0]; xm = x[-1:] + x  # xm[k] = x[k-1]
    # A[i]: pendiente [i..i+ln-1] en x[i-1]; B[i]: mismo pendiente en x[i+ln]
    A, B = [INF, 0], [INF, INF]
    for ln in range(K - 2, -1, -1):
        xr = x[ln + 1:]
        A, B = [INF] + [max(min(a + xa - xb, b + xc - xa), tt)
                        for a, b, xa, xb, xc, tt in zip(A, B, x, xm, xr, t)], \
               [max(min(a + xa - xb, b + xc - xa), tt)
                for a, b, xa, xb, xc, tt in zip(A, B, x[ln:], xm, xr, t[ln:])] + [INF]
    print(min(min(A), min(B)))
main()
