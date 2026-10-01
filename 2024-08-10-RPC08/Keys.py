# Una tecla por cada cambio de letra (sin importar mayuscula) o espacio, mas un shift
# por cada bloque de mayusculas (los espacios no rompen el bloque, las minusculas si).
s = input().rstrip("\n")
cost = 0; prev = None; shift = False
for ch in s:
    k = ch.lower()
    if k != prev:
        cost += 1
    prev = k
    if ch.isupper():
        if not shift: cost += 1; shift = True
    elif ch.islower():
        shift = False
print(cost)
