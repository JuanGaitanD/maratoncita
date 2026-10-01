# Greedy: el siguiente ganador w es el unico cuyo numero esta al frente de las dos listas
# donde aparece (las de los otros dos jugadores). O(total).
import sys
def main():
    s = sys.stdin.read().split()
    p = [0, 0, 0]
    total = (len(s[0]) + len(s[1]) + len(s[2])) // 2
    head = lambda i: s[i][p[i]] if p[i] < len(s[i]) else ''
    out = []
    for _ in range(total):
        for w in range(3):
            a, b = [i for i in range(3) if i != w]
            c = str(w + 1)
            if head(a) == c and head(b) == c:
                p[a] += 1; p[b] += 1; out.append(c); break
    print(''.join(out))
main()
