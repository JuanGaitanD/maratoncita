# Sumar las longitudes de los tramos de cada punto de partida; el equipo camina a la
# velocidad del mas lento. Respuesta: min sobre puntos de ceil(suma / vmin). Varios casos hasta EOF.
import sys
lines = sys.stdin.read().split("\n")
out, p = [], 0
while p < len(lines) and lines[p].strip():
    n, s = map(int, lines[p].split()); p += 1
    tot = {}
    for _ in range(s):
        a, b, d = map(int, lines[p].split()); p += 1
        tot[a] = tot.get(a, 0) + d
    v = min(map(int, lines[p].split())); p += 1
    out.append(str(min((t + v - 1) // v for t in tot.values())))
print("\n".join(out))
