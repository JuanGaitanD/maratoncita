# Dijkstra sobre residuos mod m = min(S): d[r] = menor posicion alcanzable = r (mod m); desde ahi
# todo r + t*m tambien lo es. Aristas: +s_i, y saltos de agujero x -> x+delta (delta <= K) con
# x = 0 mod p_j, x+delta = 0 mod p_k: el menor x >= d[r] sale por CRT. Respuesta max(d) - m.
import sys, heapq
from math import gcd
def crt(a1, m1, a2, m2):
    g = gcd(m1, m2)
    if (a2 - a1) % g: return None
    l = m1 // g * m2
    t = (a2 - a1) // g * pow(m1 // g, -1, m2 // g) % (m2 // g)
    return (a1 + m1 * t) % l, l
def main():
    v = list(map(int, sys.stdin.read().split()))
    S, P, K = v[0], v[1], v[2]
    s = v[3:3 + S]; p = v[3 + S:3 + S + P]
    m = min(s)
    combos = set()
    for a in p:
        for b in p:
            for dl in range(1, K + 1):
                c = crt(0, a, -dl % b, b)
                if c: combos.add((c[0], c[1], dl))
    pre = []                                # datos para combinar con x = r (mod m)
    for c2, M2, dl in combos:
        g = gcd(m, M2); Mg = M2 // g
        pre.append((c2, g, Mg, pow(m // g, -1, Mg) if Mg > 1 else 0, m * Mg, dl))
    INF = float("inf")
    d = [INF] * m; d[0] = 0
    pq = [(0, 0)]
    while pq:
        du, r = heapq.heappop(pq)
        if du > d[r]: continue
        for st in s:
            y = du + st
            if y < d[y % m]: d[y % m] = y; heapq.heappush(pq, (y, y % m))
        for c2, g, Mg, inv, L, dl in pre:
            diff = c2 - r
            if diff % g: continue
            x = r + m * (diff // g * inv % Mg)
            if x < du: x += (du - x + L - 1) // L * L
            y = x + dl
            if y < d[y % m]: d[y % m] = y; heapq.heappush(pq, (y, y % m))
    mx = max(d)
    print(-1 if mx == INF or mx - m <= 0 else mx - m)
main()
