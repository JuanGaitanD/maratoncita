def desencriptar(row):
    if len(row) / 4 == 1:
        return "v"
    else:
        return "w"

n = int(input())
row1 = input()
row2 = input()
answer = ""
ram = 0

for i in range(n):
    if row1[i] == row2[i]:
        answer += desencriptar(row1[ram:i])
        ram = i + 1

answer += desencriptar(row1[ram:n])

print(answer)