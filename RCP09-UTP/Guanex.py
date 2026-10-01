# Se mantienen los extremos (a, b) del diametro. Al agregar una hoja x solo puede cambiar a (x, a) o (x, b):
# distancias con LCA por binary lifting (la hoja nueva extiende las tablas en O(log)). Diametro inicial: doble BFS.
import sys
def main():
    d = sys.stdin.buffer.read().split()
    n = int(d[0]); MAXV = 300001; LOG = 19
    adj = {}
    p = 1
    for _ in range(n - 1):
        u, v = int(d[p]), int(d[p + 1]); p += 2
        adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
    root = int(d[1])
    depth = [0] * MAXV
    up0 = [root] * MAXV
    order = [root]; seen = {root}
    for v in order:
        for u in adj[v]:
            if u not in seen:
                seen.add(u); depth[u] = depth[v] + 1; up0[u] = v; order.append(u)
    up = [up0]
    for k in range(1, LOG):
        pr = up[-1]
        up.append([pr[pr[v]] for v in range(MAXV)])
    def dist(x, y):
        dx, dy = depth[x], depth[y]
        res = dx + dy
        if dx < dy: x, y, dx, dy = y, x, dy, dx
        diff = dx - dy; k = 0
        while diff:
            if diff & 1: x = up[k][x]
            diff >>= 1; k += 1
        if x != y:
            for k in range(LOG - 1, -1, -1):
                uk = up[k]
                if uk[x] != uk[y]: x = uk[x]; y = uk[y]
            x = up0[x]
        return res - 2 * depth[x]
    a = max(order, key=lambda v: depth[v])
    b = max(order, key=lambda v: dist(a, v))
    diam = dist(a, b)
    out = [diam]
    q = int(d[p]); p += 1
    for _ in range(q):
        x, y = int(d[p]), int(d[p + 1]); p += 2
        depth[x] = depth[y] + 1
        up0[x] = y
        for k in range(1, LOG):
            up[k][x] = up[k - 1][up[k - 1][x]]
        da, db = dist(x, a), dist(x, b)
        if da >= db and da > diam: diam = da; b = x
        elif db > diam: diam = db; a = x
        out.append(diam)
    print("\n".join(map(str, out)))
main()
