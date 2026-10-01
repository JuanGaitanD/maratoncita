def get_fifty(lista):
    return sum(lista)/2

n = int(input())

candidates = list(map(int, input().split()))    

fifty = get_fifty(candidates)
top = candidates.pop(candidates.index(max(candidates)))

if (top > fifty):
    print('IMPOSSIBLE TO WIN')
else: 
    meta = candidates.pop(candidates.index(max(candidates)))
    layers = 0
    ram = 0

    for i in sorted(candidates):
        if (i == ram):
            meta += i
            continue

        meta += i
        ram = i
        if (meta > fifty ):
            layers += 1
            print(layers)
            break
        else:
            layers += 1

# import math as mt

# n = int(input())
# candidates = sorted(map(int, input().split()))

# total = mt.floor(sum(candidates) / 2)
# candidates.pop(candidates.index(min(candidates)))
# pasos = 0
# second = candidates[len(candidates)-2]
# while (second < total):
#     print(f"{candidates} {sum(candidates)} {total} {pasos}")
#     pasos += 1
#     if (second >= total):
#         break
    
#     total = mt.floor(sum(candidates) / 2)
#     candidates.pop(candidates.index(min(candidates)))
#     print(f"{candidates} {sum(candidates)} {total} {pasos}")


# print(pasos)
