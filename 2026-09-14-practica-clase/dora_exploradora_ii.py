x, y = map(int, input().split())

def obtener_valor(diagonal, coordenada_x_o_y):
    return int(( (d-1)*d/2 ) + 1 + diagonal - coordenada_x_o_y)

while (x!=0):
    d = x + y - 1

    if (d % 2 == 0):
        print(obtener_valor(d, y))
    else:
        print(obtener_valor(d, x))
    
    x, y = map(int, input().split()) 
