# Se resuelve con el algoritmo de Programación Dinamica sobre Digitos (Digit DP)
# Joder lo que costó esto jajaja

MODULO = 10007

# Calcular si es twin me ahorra tener que restar uno al digito de l
def isTwin(x):
    x = str(x)

    if len(x) % 2 != 0:
        return False

    for i in range(1, len(x), 2):
        if x[i] != x[i-1]:
            return False
    return True

def potencia_con_modulo(x, exponente):
    resultado = 1
    x %= MODULO

    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * x) % MODULO
        x = (x*x) % MODULO
        exponente //= 2
    
    return resultado

# Main función
def get_twins(m):
    m = list(map(int, m))
    suma = 0

    longitud_m = len(m)
    
    # Contamos los casos normales menos los que tengan dos digitos o los del final (99)
    for i in range(2, longitud_m, 2):
        k = i // 2
        ram = (9 * potencia_con_modulo(10, k - 1)) % MODULO
        suma = (suma + ram) % MODULO

    if longitud_m % 2 == 0:
        # Ahora vamos a contar los casos que pueden variar
        k = longitud_m//2

        for i in range(k):
            limite = m[2*i]
            
            if i == 0:
                digito = 1 
            else: 
                digito = 0
            
            for _ in range(digito, limite):
                suma = (suma + potencia_con_modulo(10, k - 1 - i)) % MODULO


            if limite > m[2 * i + 1]:
                break

            if limite < m[2 * i + 1]:
                suma = (suma + potencia_con_modulo(10, k - 1 - i)) % MODULO
                break

            if i == k-1:
                suma = (suma + 1) % MODULO

    return int(suma)

#Operación sin más
n = input()
m = input()
resultado = 0

if isTwin(n):
    resultado += 1

n = get_twins(n)
m = get_twins(m)

resultado = (resultado+m-n+MODULO) % (10007)

print(resultado)