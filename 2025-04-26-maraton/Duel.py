# Greedy con dos punteros sobre manos ordenadas: max victorias de Alice = emparejamientos
# donde su carta supera a la de Bob; min de Alice = n - max victorias de Bob.
import sys
d = list(map(int, sys.stdin.read().split()))
n = d[0]
alice = sorted(d[1:n + 1])
s = set(alice)
bob = [x for x in range(1, 2 * n + 1) if x not in s]
def wins(h1, h2):
    w = 0
    for x in h1:
        if x > h2[w]:
            w += 1
    return w
print(n - wins(bob, alice), wins(alice, bob))
