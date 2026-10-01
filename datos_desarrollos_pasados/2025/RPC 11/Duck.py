def evaluar_distribucion_balls(data):
    if max(data) == min(data) and len(data) % 3 == 0:
        return True
    else:
        while True:
            data = [x for x in data if x != 0]

            if len(data) < 3:
                if len(data) == 0:
                    return True
                return False
            
            data.sort(reverse=True)

            data[0] -= 1
            data[1] -= 1
            data[2] -= 1

ducks = []
for _ in range(int(input())):
    ducks.append(int(input()))

if (evaluar_distribucion_balls(ducks)):
    print("YES")
else:
    print("NO")