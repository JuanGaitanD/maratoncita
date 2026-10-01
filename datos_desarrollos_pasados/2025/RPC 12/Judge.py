n, m = map(int, input().split())
judge_vacations = []
count = 0

for _ in range(n):
    data = list(map(int, input().split()))
    range_vacations = []
    for i in range(1, len(data), 2):
        range_vacations += list(range(data[i], data[i+1]+1))
    
    judge_vacations.append(range_vacations)

for f in range(1, m+1):
    count_judges = n
    
    for judge in judge_vacations:
        if f in judge:
            count_judges -= 1
    
    if count_judges >= 3:
        count += 1

print(count)