# Solo el primer termino tiene signo esperado no nulo (+/- equiprobables se cancelan).
# Si el primer termino acaba en el digito j aporta S_j = sum_{i<=j} d_i*10^-i (prob 0.9, o 1 si es el ultimo).
import sys
s = sys.stdin.readline().strip()
acc, p, e = 0.0, 1.0, 0.0
for i, ch in enumerate(s):
    acc += int(ch) * p
    p /= 10
    e += acc * (0.9 if i < len(s) - 1 else 1.0)
print("%.9f" % e)
