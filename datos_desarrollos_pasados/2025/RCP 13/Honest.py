from collections import Counter

n = int(input())
base = [0] * 50
resultado = ""

for _ in range(n*10):
    ram_list = list(map(int, input().split()))

    for number in ram_list:
      if base[number-1] == 0:
         base[number-1] = [1, number]
      else:
        base[number-1] = [base[number-1][0] + 1, number]

for f in base:
    if f == 0:
       continue
    if f[0] <= 2*n:
      continue
    
    resultado += str(f[1]) + " "

if resultado == "":
   print(-1)
else:
    print(resultado.strip())