import sys, itertools
w, d = map(int, sys.stdin.read().split()); t = 0
for s in itertools.product('ABC', repeat=w):
    s = ''.join(s)
    if 'AA' in s or 'CC' in s or 'BBB' in s or s == s[::-1]: continue
    c = [s.count(x) for x in 'ABC']
    if max(c) - min(c) <= d: t += 1
print(t)
