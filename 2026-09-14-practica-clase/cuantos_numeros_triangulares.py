num, num2 = map(int, input().split())

def get_position_triangular_number(n, roundUp):
    result = ( -1 + ( 1+(8*n) )**0.5  ) / 2
    if (roundUp): 
        return int(-( -(result) // 1 ))
    else:
        return int(result // 1)

while (num != 0):
    print(-get_position_triangular_number(num, True)+get_position_triangular_number(num2, False)+1)
    
    num, num2 = map(int, input().split())
