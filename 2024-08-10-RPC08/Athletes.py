# La palabra (en minusculas) debe ser no decreciente o no creciente.
s = input().strip().lower()
print("yes" if list(s) == sorted(s) or list(s) == sorted(s, reverse=True) else "no")
