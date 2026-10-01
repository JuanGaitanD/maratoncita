# Las B/C forman m segmentos alternantes separados por las A (|m - a| <= 1).
# Segmentos: p con una B extra, q con una C extra, r balanceados (2 formas, >= 1 par).
# Formas = sum m!/(p!q!r!) * 2^r * C(T - r + m - 1, m - 1) * (2 si m == a), T = b - p pares.
a, b, c = map(int, input().split())
M = 10 ** 9 + 7
F = [1] * 700
for i in range(1, 700):
    F[i] = F[i - 1] * i % M
I = [pow(f, M - 2, M) for f in F]
def comb(x, y):
    return 0 if y < 0 or x < y or x < 0 else F[x] * I[y] * I[x - y] % M
ans = 0
for m in range(max(1, a - 1), a + 2):
    mult = 2 if m == a else 1
    for p in range(m + 1):
        q = p - (b - c); r = m - p - q; T = b - p
        if q < 0 or r < 0 or T < r:
            continue
        ways = F[m] * I[p] * I[q] * I[r] * pow(2, r, M) * comb(T - r + m - 1, m - 1)
        ans = (ans + ways * mult) % M
print(ans)
