# Menor k con 32*2^k >= |s|; se imprime "long" k+1 veces.
import sys
m = len(sys.stdin.readline().strip()); c, k = 32, 1
while c < m: c *= 2; k += 1
print(" ".join(["long"] * k))
