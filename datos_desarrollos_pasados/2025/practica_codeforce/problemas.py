# Bubble sort algorithm
lista = [6, 5, 1, 3, 6, 6, 3, 2, 53, 12]

def bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):
        # n - i - 1 es porque vamos a ir hasta el último elemento más la iteración que llevemos
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

print(bubble_sort(lista))

# n, q = map(int, input().split())

# data = list(map(int, input().split()))

# x = []
# y = []
# z = []

# for i in range(q):
#     operator, l, r = input().split()

#     if operator == "c":
#         print("c", l, r)
#     elif operator == "s":
#         print("s", l, r)
#     else:
#         print("Error con la consulta")