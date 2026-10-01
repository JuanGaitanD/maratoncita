# Fuerza bruta: DP sobre automata KMP (O(N*m*K)) contra Festival.py en casos pequenos.
import random, subprocess, sys
M = 10**9 + 7
def brute(N, K, S):
    m = len(S); al = [chr(97 + i) for i in range(K)]
    def go(st, ch):
        s = S[:st] + ch
        while s and not S.startswith(s): s = s[1:]
        return len(s)
    T = [[go(st, ch) for ch in al] for st in range(m)]
    dp = [0] * (m + 1); dp[0] = 1
    for _ in range(N):
        nd = [0] * (m + 1); nd[m] = dp[m] * K % M
        for st in range(m):
            for nx in T[st]: nd[nx] = (nd[nx] + dp[st]) % M
        dp = nd
    return dp[m]
for _ in range(300):
    K = random.randint(1, 3); m = random.randint(1, 5); N = random.randint(m, 12)
    S = "".join(random.choice("abc"[:K]) for _ in range(m))
    out = subprocess.run([sys.executable, "Festival.py"], input=f"{N} {K} {S}\n", capture_output=True, text=True).stdout.strip()
    if int(out) != brute(N, K, S): print("BAD", N, K, S, out); break
else: print("ok")
# caso grande 'a'*1000
dp = [0] * 1001; dp[0] = 1
for _ in range(10000):
    nd = [0] * 1001; nd[0] = sum(dp[:1000]) * 25 % M; nd[1000] = dp[1000] * 26 % M
    for st in range(1000): nd[st + 1] = (nd[st + 1] + dp[st]) % M
    dp = nd
print("big", dp[1000])
