import math 

while(True):
    N, S = map(int, input().split()) 
    nodos = {}  
    result = 200

    for i in range(S): 
        temp = list(map(int, input().split())) 
        v = str(temp[0])
        if(v in nodos):
            nodos[f"{temp[0]}"].append(temp)
        else:
            nodos.update({f"{temp[0]}": [temp]}) 

    velocidad_caminar = list(map(int, input().split()))
    velocidad_caminar = sorted(velocidad_caminar)
    lower_case = velocidad_caminar[0]

    # print(nodos)

    for i in nodos: 
        result_temp = 0
        n = str(i)

        for j in nodos[n]: 
            tiempo = j[2] / lower_case
            result_temp += tiempo
        
        if(result_temp < result):
            result = result_temp

    result = math.ceil(result)

    print(result)