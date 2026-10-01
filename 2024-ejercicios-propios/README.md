# Ejercicios propios 2024

- Fecha: 2024
- Juez: ninguno. Sin juez: ejercicios de práctica estilo CodeAbbey guardados en `datos_desarrollos_pasados/2024/Own/*.docx`. Enunciados reconstruidos.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Fibonacci divisibility | `FibonacciDivisibility.py` / `FibonacciDivisibility.cpp` | Fibonacci modular | O(n·P(M)) | local-ok |
| B | Greatest common divisor | `GreatestCommonDivisor.py` / `GreatestCommonDivisor.cpp` | Euclides | O(n log V) | local-ok |
| C | Pitágoras (tipo de triángulo) | `Pitagoras.py` / `Pitagoras.cpp` | Geometría entera | O(n) | local-ok |
| D | Sum of digits | `SumOfDigits.py` / `SumOfDigits.cpp` | Aritmética | O(n·d) | local-ok |
| E | Maximum of array | `MaximumOfArray.py` / `MaximumOfArray.cpp` | Recorrido lineal | O(n) | local-ok |
| F | Median of three | `MedianOfThree.py` / `MedianOfThree.cpp` | Ordenamiento | O(n) | local-ok |
| G | Minimum of two | `MinimumOfTwo.py` / `MinimumOfTwo.cpp` | Comparación | O(n) | local-ok |
| H | Triangles | `Triangles.py` / `Triangles.cpp` | Desigualdad triangular | O(n) | local-ok |

## Fibonacci divisibility (`FibonacciDivisibility`)

**Enunciado:** Se dan N números M. Para cada uno, imprimir el menor índice i > 0 tal que F(i) es divisible por M (F(0)=0, F(1)=1). (enunciado reconstruido a partir del código del usuario)

**Solución:** El código original usaba una lista fija de 29 Fibonacci, que falla para M grandes. Basta con generar la sucesión módulo M: guardamos el par (F(i), F(i+1)) reducido módulo M y avanzamos hasta que F(i) ≡ 0. Trabajar módulo M mantiene los números pequeños y es correcto porque la divisibilidad solo depende del residuo. La sucesión módulo M es periódica (período de Pisano) y siempre contiene un cero, así que el ciclo termina, a lo sumo en unas 6M iteraciones. Para cada consulta el costo es lineal en el índice encontrado, con memoria constante. Las respuestas se imprimen en una línea separadas por espacio.

## Greatest common divisor (`GreatestCommonDivisor`)

**Enunciado:** Se dan N pares (a, b). Para cada par imprimir "(mcd mcm)", separados por espacios. (enunciado reconstruido a partir del código del usuario)

**Solución:** El usuario usaba el algoritmo de Euclides por restas, que puede ser muy lento si un número es mucho mayor que el otro. Aquí se usa la versión con módulo: mcd(a, b) = mcd(b, a mod b), que termina en O(log) pasos. El mínimo común múltiplo se obtiene con la identidad mcd·mcm = a·b; para evitar desbordes en C++ se calcula como a / mcd · b, dividiendo primero. En Python se usa math.gcd. Cada par se imprime entre paréntesis y los pares se separan con un espacio, todo en una sola línea de salida.

## Pitágoras (tipo de triángulo) (`Pitagoras`)

**Enunciado:** Para N triángulos con catetos a, b y lado mayor c, imprimir R si es rectángulo, A si es acutángulo y O si es obtusángulo. (enunciado reconstruido a partir del código del usuario)

**Solución:** El código original usaba sqrt y pow en punto flotante y truncaba a entero, lo que puede clasificar mal. La versión nueva compara en enteros c² con a² + b²: si son iguales el ángulo opuesto a c es recto (R), si c² es menor el ángulo es agudo (A) y si es mayor es obtuso (O), por la ley de los cosenos. Usamos long long para que los cuadrados no desborden. Se quitaron los mensajes de entrada ("Ingrese...") porque un juez solo espera la salida pedida. Las letras se imprimen separadas por espacios en una línea.

## Sum of digits (`SumOfDigits`)

**Enunciado:** Para N tríos (a, b, c), calcular a·b + c e imprimir la suma de sus dígitos. (enunciado reconstruido a partir del código del usuario)

**Solución:** Es simulación directa. Se calcula v = a·b + c y se suman sus dígitos tomando v mod 10 y dividiendo entre 10 hasta llegar a cero, igual que en el código original. En Python basta con convertir el número a cadena y sumar cada carácter como entero. En C++ se usa long long para que el producto no desborde. Si v es 0 la suma es 0, y ambos métodos lo manejan sin caso especial. La complejidad es lineal en la cantidad de dígitos de cada número. Los resultados van en una línea separados por espacio.

## Maximum of array (`MaximumOfArray`)

**Enunciado:** Se da una lista de enteros en una línea. Imprimir el máximo y el mínimo. (enunciado reconstruido a partir del código del usuario)

**Solución:** Un solo recorrido basta: mantenemos el mayor y el menor visto hasta el momento y los actualizamos con cada número leído. En C++ se lee hasta EOF con while (cin >> x), sin guardar el arreglo, así que la memoria es constante; los valores iniciales son LLONG_MIN y LLONG_MAX para que el primer número los reemplace. En Python se leen todos los tokens y se usan max y min, que también son lineales. Es la misma idea que el código original del usuario. La salida es "max min" en una línea.

## Median of three (`MedianOfThree`)

**Enunciado:** Para N tríos de enteros, imprimir el valor del medio (la mediana) de cada uno. (enunciado reconstruido a partir del código del usuario)

**Solución:** Con solo tres números lo más simple es ordenarlos y tomar el del centro. Ordenar tres elementos cuesta tiempo constante, así que el total es lineal en la cantidad de tríos. Se podría resolver con comparaciones (max(min(a,b), min(max(a,b), c))), pero ordenar es más claro y difícil de equivocar. Los valores repetidos no causan problemas: si dos son iguales, uno de ellos queda en el medio. Las medianas se imprimen separadas por espacios en una sola línea, igual que en la solución original del usuario.

## Minimum of two (`MinimumOfTwo`)

**Enunciado:** Para N pares de enteros, imprimir el menor de cada par. (enunciado reconstruido a partir del código del usuario)

**Solución:** Basta comparar los dos números de cada par y quedarse con el menor (min). El código original tenía dos problemas para un juez: imprimía mensajes como "Ingrese el número..." y, si los números eran iguales, escribía un texto en vez del valor. Si a = b el mínimo es ese mismo valor, así que no hace falta un caso especial. Se quitaron los mensajes y las respuestas se imprimen en una línea separadas por espacios. Se usa long long para soportar valores grandes y negativos.

## Triangles (`Triangles`)

**Enunciado:** Para N tríos de longitudes, imprimir 1 si se puede formar un triángulo (no degenerado) y 0 si no. (enunciado reconstruido a partir del código del usuario)

**Solución:** Tres segmentos forman un triángulo si y solo si cada uno es estrictamente menor que la suma de los otros dos (desigualdad triangular). El código original solo revisaba dos de las tres condiciones (faltaba a + c > b), así que fallaba con entradas como 1 10 1. Aquí se revisan las tres. La desigualdad estricta descarta los triángulos degenerados (por ejemplo 1 2 3, donde los tres puntos quedan alineados). Se usa long long para que las sumas no desborden, y los resultados 1/0 se imprimen separados por espacio.
