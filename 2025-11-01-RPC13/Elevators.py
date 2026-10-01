# Total = (viajes + trabajos, fijo) + esperas. Con residuos c_i (instante ideal del tramo i, mod P=2e6)
# y fase k_j por ascensor, la espera del tramo i es (c_i + k_j - W) mod P. En el optimo cada ascensor
# tiene un tramo sin espera, asi que k_j = k_j' +- (c_{i-1} - c_i) para algun otro ascensor j':
# se enumeran esos candidatos (arbol de profundidad <= 3) y para cada juego de fases se simula greedy.
import sys
def main():
    d = sys.stdin.read().split(); n = int(d[0])
    F = list(map(int, d[1:n + 1])); Tw = list(map(int, d[n + 1:2 * n + 1]))
    P = 2 * 10 ** 6; c = []; A = 0; cur = 0
    for g, tw in zip(F, Tw):
        s = cur if g > cur else (P - cur) % P
        c.append((s - A) % P); A += abs(g - cur) + tw; cur = g
    D = {(c[i - 1] - c[i]) % P for i in range(1, n)}; D |= {(-x) % P for x in D}
    best = [float("inf")]
    def run(ks):
        W = 0; lim = best[0]
        for ci in c:
            W += min((ci + k - W) % P for k in ks)
            if W >= lim: return
        best[0] = W
    k1 = (-c[0]) % P; run((k1,))
    S1 = sorted((k1 + x) % P for x in D); seen = set()
    for a, k2 in enumerate(S1):
        run((k1, k2))
        S2 = set(S1[a + 1:]) | {(k2 + x) % P for x in D}; S2.discard(k2)
        for k3 in S2:
            run((k1, k2, k3))
            S3 = S2 | {(k3 + x) % P for x in D}; S3.discard(k3)
            for k4 in S3:
                key = frozenset((k2, k3, k4))
                if key not in seen:
                    seen.add(key); run((k1, k2, k3, k4))
    print(A + best[0])
main()
