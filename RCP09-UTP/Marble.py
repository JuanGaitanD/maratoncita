# BFS sobre pares de posiciones. dest[dir][celda] = donde se detiene una canica sola (-1 si cae). Si ambas
# terminan en la misma celda, la mas cercana queda ahi y la otra justo antes; si alguna cae, el estado se descarta.
import sys
def main():
    d = sys.stdin.read().split()
    n, m = int(d[0]), int(d[1]); g = "".join(d[2:2 + n])
    r1, c1, r2, c2 = map(int, d[2 + n:6 + n])
    N = n * m
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dest = []
    for dr, dc in dirs:
        de = [-1] * N
        for v in range(N):
            if g[v] in "#O": continue
            i, j = divmod(v, m)
            while True:
                x, y = i + dr, j + dc
                if not (0 <= x < n and 0 <= y < m) or g[x * m + y] == "O": i = -1; break
                if g[x * m + y] == "#": break
                i, j = x, y
            de[v] = -1 if i < 0 else i * m + j
        dest.append((de, dr * m + dc))
    a, b = (r1 - 1) * m + c1 - 1, (r2 - 1) * m + c2 - 1
    win = [ch == "G" for ch in g]
    if win[a] and win[b]: print(0); return
    seen = bytearray(N * N); seen[a * N + b] = 1
    cur = [(a, b)]; steps = 0
    while cur:
        steps += 1; nxt = []
        for a, b in cur:
            for de, delta in dest:
                x, y = de[a], de[b]
                if x < 0 or y < 0: continue
                if x == y:
                    if abs(a - x) < abs(b - x): y = x - delta
                    else: x = y - delta
                k = x * N + y
                if seen[k]: continue
                if win[x] and win[y]: print(steps); return
                seen[k] = 1; nxt.append((x, y))
        cur = nxt
    print(-1)
main()
