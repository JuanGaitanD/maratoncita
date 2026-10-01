import sys
d = sys.stdin.read().split(); k, s = int(d[0]), d[1]
comp = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
bar = lambda x: ''.join(comp[c] for c in reversed(x))
tot = 0
for i in range(k):
    B = s[i:] + s[:i]
    for a in range(1, k):
        for b in range(1, k):
            if 2 * (a + b) == k and B == B[:a] + B[a:a+b] + bar(B[:a]) + bar(B[a:a+b]): tot += 1
            c = k // 2 - a - b
            if k % 2 == 0 and c >= 1:
                X, Y, Z = B[:a], B[a:a+b], B[a+b:a+b+c]
                if B == X + Y + Z + bar(X) + bar(Y) + bar(Z): tot += 1
print(tot)
