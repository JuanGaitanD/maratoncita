# Union-Find con tamanos: razas = componentes, y la raza mas grande = mayor tamano.
import sys
def main():
    d = sys.stdin.buffer.read().split()
    p = 0; out = []
    while True:
        n, m = int(d[p]), int(d[p + 1]); p += 2
        if n == 0 and m == 0: break
        par = list(range(n + 1)); sz = [1] * (n + 1); comp = n
        for _ in range(m):
            a, b = int(d[p]), int(d[p + 1]); p += 2
            while par[a] != a: par[a] = par[par[a]]; a = par[a]
            while par[b] != b: par[b] = par[par[b]]; b = par[b]
            if a != b:
                if sz[a] < sz[b]: a, b = b, a
                par[b] = a; sz[a] += sz[b]; comp -= 1
        out.append("%d %d" % (comp, max(sz[1:])))
    print("\n".join(out))
main()
