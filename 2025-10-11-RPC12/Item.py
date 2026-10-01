# Costo por pagina = min(alternar diferencias, 1+no deseados (Select All), 1+deseados (Deselect All)).
# Navegacion: cubrir [min,max] de paginas con trabajo desde s: (R-L) + min(|s-L|,|s-R|).
import sys
def main():
    t = list(map(int, sys.stdin.read().split()))
    n, m, s, p, q = t[:5]
    pre = [0] * (n + 1); want = [0] * (n + 1)
    for x in t[5:5 + p]: pre[x] = 1
    for x in t[5 + p:5 + p + q]: want[x] = 1
    pages = (n + m - 1) // m
    total, L, R = 0, None, None
    for g in range(1, pages + 1):
        items = range((g - 1) * m + 1, min(n, g * m) + 1)
        diff = sum(pre[i] != want[i] for i in items)
        if diff == 0: continue
        w = sum(want[i] for i in items)
        total += min(diff, 1 + len(items) - w, 1 + w)
        if L is None: L = g
        R = g
    if L is not None:
        total += (R - L) + min(abs(s - L), abs(s - R))
    print(total)
main()
