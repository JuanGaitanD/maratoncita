n = int(input())

records = list(map(int, input().split()))
a, b, c = 0, 0, 0

# Consideremos a B como el intermedio entre A y C
a = int(records[0] / 3)
c = int(records[-1] / 3)
b = 0

for p in records:
    ram = p -a -c

    if a < ram < c:
        if (ram + (2*a)) in records:
            b = ram
            break



print(a, b, c)