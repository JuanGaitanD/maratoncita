total = 0
p = [0, 0, 0]

for _ in range(int(input())):
    size, pieces = input().split()
    pieces = int(pieces)

    if (size == "S"):
        p[0] += pieces
        if (p[0] >= 6):
            total += 1
            p[0] -= 6
    elif (size == "M"):
        p[1] += pieces
        if (p[1] >= 8):
            total += 1
            p[1] -= 8
    elif (size == "L"): 
        p[2] += pieces
        if (p[2] >= 12):
            total += 1
            p[2] -= 12

if p[0] > 0:
    total += 1

if p[1] > 0:
    total += 1

if p[2] > 0: 
    total += 1

print(total)
