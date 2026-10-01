# Counter cuenta la cantidad de caracteres en una cadena y lo devuelve como un diccionario
from collections import Counter

#def isPalindromo(word):
#    return word == word[::-1]

def isTextPalidromo(text):
    text = text.strip().lower()
    data = Counter(text)

    impar_count = 0

    for a in data.values():
        if a % 2 != 0:
            impar_count += 1

    return impar_count <= 1

word = input()

if isTextPalidromo(word):
    print("yes")
else:
    print("no")