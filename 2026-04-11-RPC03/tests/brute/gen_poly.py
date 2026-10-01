import random, sys
random.seed(int(sys.argv[1])); W = int(sys.argv[2]); H = int(sys.argv[3])
hs = [random.randint(1, H) for _ in range(W)]
if random.random() < 0.3: hs = [H] * W
s = 'u' * hs[0]
for i in range(W):
    s += 'r'
    if i + 1 < W:
        dlt = hs[i + 1] - hs[i]; s += ('u' if dlt > 0 else 'd') * abs(dlt)
s += 'd' * hs[-1] + 'l' * W
r = random.randint(0, len(s) - 1); s = s[r:] + s[:r]
print(len(s), s)
