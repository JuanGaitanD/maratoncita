first = input().strip()
second = input().strip()
third = input().strip()
answer = ""

while first != "" and second != "" and third != "":
    #print(first, second, third)
    if first[0] == second[0]:
        answer += first[0]
        first = first[1:]
        second = second[1:]
    elif first[0] == third[0]:
        answer += first[0]
        first = first[1:]
        third = third[1:]
    else:
        answer += second[0]
        second = second[1:]
        third = third[1:]
    
if first == second:
    answer += first
elif first == third:
    answer += first
else:
    answer += second

print(answer)