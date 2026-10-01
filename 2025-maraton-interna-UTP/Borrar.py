# Quitar los caracteres prohibidos (dados entre corchetes) y no repetir un caracter igual
# al ultimo que quedo en el resultado; al final recortar espacios de los extremos.
import sys
lines = sys.stdin.read().split("\n")
text, banned = lines[0].rstrip("\r"), set(lines[1].strip()[1:-1])
res = []
for ch in text:
    if ch not in banned and (not res or res[-1] != ch):
        res.append(ch)
print("".join(res).strip())
