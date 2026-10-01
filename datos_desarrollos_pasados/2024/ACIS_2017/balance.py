copies, weight = map(int, input().split())
t1, t2, t3 = map(int, input().split())
result = 0

for i in range(copies+1):
    for j in range(copies+1):
        for k in range(copies+1):
            result_one = i * t1 + j * t2 + k * t3 == weight
            result_two = weight + i*t1 == j * t2 + k * t3
            result_three = weight + j*t2 == i*t1 + k*t3
            result_four = weight + k*t3 == i*t1 + j*t2


            if result_one or result_two or result_three or result_four:
                result += 1

print(result)