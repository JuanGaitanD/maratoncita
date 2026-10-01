n, m = map(int, input().split())

if n > m:
    print(0)
elif n == m:
    print(m)
else:
    print(n+1)