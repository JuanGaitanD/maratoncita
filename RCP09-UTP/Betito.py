# Flood fill (DFS iterativo) desde '*' sobre celdas que no son '#'; se cuentan las celdas alcanzadas.
import sys
def main():
    data = sys.stdin.buffer.read().split()
    p = 0; out = []
    while True:
        r, c = int(data[p]), int(data[p + 1]); p += 2
        if r == 0: break
        W = c + 2
        g = bytearray(b'#' * (W * (r + 2)))
        for i in range(r):
            g[(i + 1) * W + 1:(i + 1) * W + 1 + c] = data[p + i]
        p += r
        s = g.index(b'*')
        g[s] = 35
        st = [s]; cnt = 1
        while st:
            v = st.pop()
            for u in (v + 1, v - 1, v + W, v - W):
                if g[u] != 35:
                    g[u] = 35; cnt += 1; st.append(u)
        out.append(str(cnt))
    print("\n".join(out))
main()
