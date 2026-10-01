# Facil si al menos la mitad resolvio en la primera mitad: 2*s1 >= s2.
s1, s2 = map(int, input().split())
print("E" if 2 * s1 >= s2 else "H")
