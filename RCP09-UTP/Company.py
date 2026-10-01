# Como P[i] < i, se recorre de N a 2: tamanos (suma de dist = sum sz*(n-sz) por arista),
# altura h y diametro F(p) = max(F(hijos), h[p] + h[hijo] + 1).
import sys
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    par = [0, 0] + list(map(int, data[1:n]))
    sz = [1] * (n + 1); h = [0] * (n + 1); F = [0] * (n + 1)
    tot = 0
    for i in range(n, 1, -1):
        p = par[i]; s = sz[i]
        tot += s * (n - s)
        sz[p] += s
        c = h[i] + 1; hp = h[p]
        f = F[i] if F[i] > hp + c else hp + c
        if f > F[p]: F[p] = f
        if c > hp: h[p] = c
    sys.stdout.write(str(tot) + "\n" + " ".join(map(str, F[1:])) + "\n")
main()
