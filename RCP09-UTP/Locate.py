# Los pasillos forman un arbol: el nido es su centro (minima excentricidad), el punto medio de un diametro.
# BFS desde cualquier celda -> extremo a; BFS desde a -> extremo b y padres; el centro (o los 2) estan en la mitad.
import sys
def bfs(g, s, W):
    par = [-2] * len(g); par[s] = -1; q = [s]
    for v in q:
        for u in (v + 1, v - 1, v + W, v - W):
            if g[u] == 46 and par[u] == -2:
                par[u] = v; q.append(u)
    return q[-1], par
def main():
    d = sys.stdin.buffer.read().split()
    t = int(d[0]); p = 1; out = []
    for case in range(1, t + 1):
        H, Wd = int(d[p]), int(d[p + 1]); p += 2
        W = Wd + 2
        g = bytearray(b"#" * (W * (H + 2)))
        for i in range(H):
            g[(i + 1) * W + 1:(i + 1) * W + 1 + Wd] = d[p + i]
        p += H
        a, _ = bfs(g, g.index(b"."), W)
        b, par = bfs(g, a, W)
        path = [b]
        while par[path[-1]] != -1: path.append(par[path[-1]])
        L = len(path) - 1
        cands = {path[L // 2], path[(L + 1) // 2]}
        best = min((c % W, c // W) for c in cands)
        out.append("Case %d: %d %d" % (case, best[1], best[0]))
    print("\n".join(out))
main()
