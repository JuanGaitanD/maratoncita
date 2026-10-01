# mi codigo
# n = int(input())
# cola = []

# for i in range(n):
#     data = input()
#     y = 0

#     if "1" in data:
#         data, y = data.split(" ")

#         cola.append(int(y))
#         continue
    
#     if int(data) == 2:
#         if len(cola) != 0:
#             min_output = cola.pop(cola.index(min(cola)))
#         continue

#     if len(cola) != 0:
#         print(min(cola))
#     else:
#         print('Empty!')


# Con Fast I/O
import sys

n = int(sys.stdin.readline())
cola = []

for i in range(n):
    line = sys.stdin.readline().split()
    operation = int(line[0])

    if operation == 1:
        cola.append(int(line[1]))
        continue
    
    if operation == 2:
        if cola:
            min_output = cola.pop(cola.index(min(cola)))
        continue

    if cola:
        sys.stdout.write(str(min(cola)) + '\n')
    else:
        sys.stdout.write('Empty!\n')