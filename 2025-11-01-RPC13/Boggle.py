# DP sobre los 16 dados: estado = ultima letra puesta; caras: arriba 0, lados 1, abajo 2 giros.
# La cara Q cuenta como "QU": exige previa <= Q y deja como ultima la U.
import sys
rows = sys.stdin.read().split()
dp = {'A': 0}
for i in range(16):
    faces = [(rows[0][i], 0)] + [(rows[k][i], 1) for k in range(1, 5)] + [(rows[5][i], 2)]
    nd = {}
    for c, w in faces:
        nxt = 'U' if c == 'Q' else c
        for last, v in dp.items():
            if last <= c and nd.get(nxt, 99) > v + w:
                nd[nxt] = v + w
    dp = nd
print(min(dp.values()) if dp else "impossible")
