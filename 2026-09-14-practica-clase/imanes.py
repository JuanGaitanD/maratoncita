# Fuente: https://codeforces.com/problemset/problem/344/A

t = ""
a = ""
c = 0

for i in range(int(input())):
    a = input()

    if t != a:
        c += 1
        t = a

print(c)
