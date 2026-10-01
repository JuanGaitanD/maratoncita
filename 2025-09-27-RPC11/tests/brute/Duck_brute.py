# Fuerza bruta: greedy (repartir siempre de los 3 colores mas abundantes) vs Duck.py.
import random, subprocess, sys
def greedy(d):
    d = d[:]
    while True:
        d = sorted([x for x in d if x], reverse=True)
        if not d: return True
        if len(d) < 3: return False
        for i in range(3): d[i] -= 1
for _ in range(300):
    c = random.randint(3, 6); d = [random.randint(1, 12) for _ in range(c)]
    d[0] += (-sum(d)) % 3
    out = subprocess.run([sys.executable, "Duck.py"], input=f"{c}\n" + "\n".join(map(str, d)) + "\n", capture_output=True, text=True).stdout.strip()
    if (out == "YES") != greedy(d): print("BAD", d); break
else: print("ok")
