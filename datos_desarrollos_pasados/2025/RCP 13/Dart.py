n, r, c = map(int, input().split())

o = n//2 + 1

if r == o and c == o:
    print(100)
else:
    ram = 100 - (max(max(o, r) - min(o, r), max(o, c) - min(o, c)) * 10)

    if ram < 0:
        print(0)
    else:
        print(ram)