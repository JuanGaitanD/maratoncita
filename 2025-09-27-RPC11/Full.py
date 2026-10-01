# Full house: las frecuencias de los digitos ordenadas son exactamente [2, 3].
from collections import Counter
s = input().strip()
print("YES" if sorted(Counter(s).values()) == [2, 3] else "NO")
