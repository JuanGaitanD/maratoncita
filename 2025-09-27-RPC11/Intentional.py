# Cada problema con numero impar de paginas deja una pagina en blanco.
import sys
a = list(map(int, sys.stdin.read().split()))
print(sum(x % 2 for x in a[1:a[0] + 1]))
