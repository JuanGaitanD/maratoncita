# Respuesta directa: k^2 mod (10^18 + 3). Python maneja enteros grandes.
import sys
d = sys.stdin.buffer.read().split()
M = 10**18 + 3
sys.stdout.write("".join(str(int(k) ** 2 % M) + "\n" for k in d[1:1 + int(d[0])]))
