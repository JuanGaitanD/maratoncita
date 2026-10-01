# Puntaje = 100 - 10 * (distancia de Chebyshev al centro), minimo 0.
n, r, c = map(int, input().split())
o = n // 2 + 1
print(max(0, 100 - 10 * max(abs(r - o), abs(c - o))))
