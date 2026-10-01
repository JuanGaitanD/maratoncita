# Para cada vector v = P - A: B debe cumplir B.v = A.v y C debe cumplir C.v = P.v = A.v + |v|^2.
# Por cada v con algun par (A, P): histogramas de B.v y C.v y suma cntB[A.v] * cntC[A.v + |v|^2].
import sys


def main():
    tok = [t for t in sys.stdin.read().split() if t != '-']
    n = int(tok[0])
    As, Ps, Bs, Cs = [], [], [], []
    for z in range(n):
        for y in range(n):
            row = tok[1 + z * n + y]
            for x in range(n):
                ch = row[x]
                if ch == 'A':
                    As.append((x, y, z))
                elif ch == 'P':
                    Ps.append((x, y, z))
                elif ch == 'B':
                    Bs.append((x, y, z))
                elif ch == 'C':
                    Cs.append((x, y, z))
    if not Bs or not Cs:
        print(0)
        return
    vecs = {}
    for ax, ay, az in As:
        for px, py, pz in Ps:
            v = (px - ax, py - ay, pz - az)
            if v != (0, 0, 0):
                vecs.setdefault(v, []).append((ax, ay, az))
    ans = 0
    for (dx, dy, dz), pts in vecs.items():
        hb, hc = {}, {}
        for x, y, z in Bs:
            k = x * dx + y * dy + z * dz
            hb[k] = hb.get(k, 0) + 1
        for x, y, z in Cs:
            k = x * dx + y * dy + z * dz
            hc[k] = hc.get(k, 0) + 1
        vv = dx * dx + dy * dy + dz * dz
        for x, y, z in pts:
            k = x * dx + y * dy + z * dz
            ans += hb.get(k, 0) * hc.get(k + vv, 0)
    print(ans)


main()
