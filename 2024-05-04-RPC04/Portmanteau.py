# Simulacion directa de las reglas: prefijo hasta la primera vocal (desde la 2a letra),
# sufijo hasta la primera vocal hacia la izquierda, y vocal de union v2, v1 u 'o'.
w1, w2 = input().strip(), input().strip()
V = "aeiou"
i = 1
while i < len(w1) and w1[i] not in V:
    i += 1
v1 = w1[i] if i < len(w1) else ""
j = len(w2) - 2
while j >= 0 and w2[j] not in V:
    j -= 1
v2 = w2[j] if j >= 0 else ""
print(w1[:i] + (v2 or v1 or "o") + w2[j + 1:])
