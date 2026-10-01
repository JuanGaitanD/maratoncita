val = input()
oc = input()
new = oc[1:-1]
temp = ""
resultado = ""

for s in val:
    if s not in new:
        if s != temp:
            resultado += s
            temp = s

resultado = resultado.strip()
print(resultado)