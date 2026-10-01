# Fila 2 con altura s_j: s_1..s_{j-1} van en fila 1 con s_j..s_{2j-2} de pareja y el resto
# se empareja de a dos consecutivos (ancho s_{2j-1}+s_{2j+1}+...). Probar todo j.
import sys
d = sys.stdin.buffer.read().split()
N = int(d[0]); s = [0] + list(map(int, d[1:1 + 2 * N]))
alt = [0] * (2 * N + 3)
for i in range(2 * N, 0, -1): alt[i] = s[i] + alt[i + 2]
best = None; pre = 0
for j in range(2, N + 2):
    pre += s[j - 1]
    v = (s[1] + s[j]) * (pre + alt[2 * j - 1])
    if best is None or v < best: best = v
print(best)
