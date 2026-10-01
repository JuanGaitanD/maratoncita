# Se puede formar palindromo si a lo sumo una letra aparece un numero impar de veces.
import sys
from collections import Counter
s = sys.stdin.readline().strip()
print("yes" if sum(v & 1 for v in Counter(s).values()) <= 1 else "no")
