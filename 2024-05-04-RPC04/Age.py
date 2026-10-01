# Probar todos los a >= 1: (D - a*A) debe ser positivo y divisible por K.
d, A, K = map(int, input().split())
print(1 if any((d - a * A) % K == 0 for a in range(1, d // A + 1) if d - a * A > 0) else 0)
