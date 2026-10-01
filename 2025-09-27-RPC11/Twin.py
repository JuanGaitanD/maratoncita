# Un twin de 2m digitos equivale a su "mitad" de m digitos (sin cero inicial).
# f(X) = twins <= X: todos los de longitud menor (10^m - 1) + mitades h con twin(h) <= X.
import sys
M = 10007

def f(x):
    L = len(x)
    full = pow(10, L // 2 - (L % 2 == 0), M) - 1     # twins con menos digitos
    if L % 2:
        return full
    h, ok = 0, True                    # h = mayor mitad valida (mod M); ok = no se anula
    m = L // 2
    for i in range(m):
        a, b = x[2 * i], x[2 * i + 1]
        if a == b:
            h = (h * 10 + int(a)) % M
            continue
        d = int(a) if a < b else int(a) - 1
        if i == 0 and d == 0:
            ok = False
        h = (h * 10 + d) % M
        h = (h * pow(10, m - i - 1, M) + pow(10, m - i - 1, M) - 1) % M  # resto con 9s
        break
    if not ok:
        return full
    return (full + h - pow(10, m - 1, M) + 1) % M

def twin(x):
    return len(x) % 2 == 0 and all(x[i] == x[i + 1] for i in range(0, len(x), 2))

lo, hi = sys.stdin.read().split()
print((f(hi) - f(lo) + twin(lo)) % M)
