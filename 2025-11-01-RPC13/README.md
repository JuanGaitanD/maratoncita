# RPC 13 de 2025: Competitive Programming Network, 13th Activity

Fecha: 2025-11-01

Juez: https://redprogramacioncompetitiva.com/contests/2025/13

Soluciones en Python 3 y C++11. Las pruebas están en `tests/`: los ejemplos del enunciado más un caso extra `.9`, contrastado con fuerza bruta cuando aplica. Para correrlas desde la raíz del repo: `python tools/test.py 2025-11-01-RPC13`.

En los problemas con salida real (A, I), los `.out` guardan la salida del programa con 9 decimales; coincide con el valor del enunciado dentro de la tolerancia pedida.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Accidental Arithmetic | [`Accidental.py`](Accidental.py) / [`Accidental.cpp`](Accidental.cpp) | Probabilidad / linealidad de la esperanza | O(L) | local-ok |
| B | Boggle Sort | [`Boggle.py`](Boggle.py) / [`Boggle.cpp`](Boggle.cpp) | DP | O(16·6·26) | local-ok |
| C | Coherency | [`Coherency.py`](Coherency.py) / [`Coherency.cpp`](Coherency.cpp) | Geometría + rejilla hash + DSU | O(n·k), k = vecinos por celda | local-ok |
| D | Dart Game | [`Dart.py`](Dart.py) / [`Dart.cpp`](Dart.cpp) | Implementación | O(1) | local-ok |
| E | Excruciating Elevators | [`Elevators.py`](Elevators.py) / [`Elevators.cpp`](Elevators.cpp) | Residuos modulares + enumeración de fases ancladas | ~1e8 (C++ 0.6 s) | local-ok (py ~8 s: usar C++) |
| F | Fences Make Good Neighbors | [`Fences.py`](Fences.py) / [`Fences.cpp`](Fences.cpp) | DP de intervalos (triangulación de polígono convexo) | O(n^3) | local-ok (Python lento: usar C++ en el juez) |
| G | Geometry Rush | [`Geometry.py`](Geometry.py) / [`Geometry.cpp`](Geometry.cpp) | Barrido por columnas / intervalos | O(w + n + m) | local-ok |
| H | Honest (or dishonest) Lottery | [`Honest.py`](Honest.py) / [`Honest.cpp`](Honest.cpp) | Conteo | O(n) | local-ok |
| I | Intermill Logistics | [`Intermill.py`](Intermill.py) / [`Intermill.cpp`](Intermill.cpp) | Greedy + ordenamiento | O(n log n) | local-ok |
| J | Jump ... Triple Jump | [`Jump.py`](Jump.py) / [`Jump.cpp`](Jump.cpp) | Fuerza bruta | O(1000) | local-ok |
| K | Knowing the Clock | [`Knowing.py`](Knowing.py) / [`Knowing.cpp`](Knowing.cpp) | Matemática | O(1) | local-ok |
| L | Linguistic Labyrinth | [`Labyrinth.py`](Labyrinth.py) / [`Labyrinth.cpp`](Labyrinth.cpp) | Conteo en retícula 3D | O(n^3·(2n)^3) | local-ok (Python lento: usar C++ en el juez) |
| M | Marching Orders | [`Marching.py`](Marching.py) / [`Marching.cpp`](Marching.cpp) | CRT generalizado | O(n^2) | local-ok |

## A. Accidental Arithmetic

**Enunciado.** Se teclea un número de hasta 1000 dígitos y entre cada par de dígitos puede aparecer un + (45 %), un − (45 %) o nada (10 %). Hay que dar el valor esperado de la expresión resultante.

**Solución.** Por linealidad de la esperanza, cada término que no es el primero lleva signo + o − con igual probabilidad, así que su aporte esperado es cero. Solo importa el primer término. Si termina en el dígito j (probabilidad 0.1^j·0.9, o 0.1^(L−1) si llega al final), vale el prefijo de j+1 dígitos. Al multiplicar ese valor por 0.1^j queda S_j = Σ_{i≤j} d_i·10^(−i). La respuesta es 0.9·Σ_{j<L−1} S_j + S_(L−1). Se recorre el número una sola vez acumulando S_j en punto flotante; las potencias negativas que se vuelven cero no afectan la precisión pedida.

## B. Boggle Sort

**Enunciado.** Hay 16 dados con 6 letras. Subir una cara lateral cuesta 1 giro y subir la de abajo cuesta 2. Se pide el mínimo de giros para que las caras de arriba queden en orden alfabético, donde la Q cuenta como "QU".

**Solución.** Se recorren los dados en orden con una DP: el estado es la última letra colocada y el valor, el mínimo de giros. Para cada dado se prueban sus 6 caras: arriba cuesta 0, cada lateral 1 y la de abajo 2. Una cara c solo se puede poner si la letra anterior es ≤ c. La cara Q se trata como el par "QU": exige anterior ≤ Q y deja U como última letra, así que el siguiente dado debe ser ≥ U. Se arranca con 'A' como última letra. Si al final no queda ningún estado alcanzable, se imprime impossible. Son 16·6·26 transiciones.

## C. Coherency

**Enunciado.** Hay n ≤ 2·10^5 bases circulares. Dos modelos están unidos si sus bordes quedan a ≤ 2 pulgadas (50.8 mm). La unidad es coherente si el grafo es conexo y, cuando n ≥ 7, todos tienen grado ≥ 2.

**Solución.** Dos modelos son vecinos si la distancia entre centros es ≤ (d1+d2)/2 + 50.8. Multiplicando por 20 y elevando al cuadrado queda la comparación entera 400·dist² ≤ (10·(d1+d2)+1016)², sin errores de redondeo. Con diámetro máximo 160, dos vecinos están a menos de 211 mm, así que los centros se agrupan en celdas de 211 mm y solo se comparan celdas adyacentes (la mitad del vecindario, para no repetir pares). Como las bases no se solapan, cada celda tiene pocos modelos. Un DSU cuenta las componentes y, de paso, los grados. Es coherente si hay una sola componente y, con n ≥ 7, el grado mínimo es ≥ 2.

*Rendimiento:* en el peor caso local, C++ tarda 1.2 s o menos; Python tarda entre 5 y 8 s y puede pasarse del límite de tiempo.

## D. Dart Game

**Enunciado.** En una cuadrícula n×n con n impar, el centro vale 100 y cada anillo hacia afuera vale 10 menos. Dada la celda donde cae el dardo, imprimir el puntaje.

**Solución.** El anillo de una celda es su distancia de Chebyshev al centro o = n/2+1, es decir, max(|r−o|, |c−o|). El centro tiene distancia 0 y vale 100; cada anillo resta 10 puntos. Como n ≤ 21, el anillo más lejano es el 10 y vale 0. La fórmula max(0, 100 − 10·dist) cubre todos los casos, incluso el de no bajar de cero. Es una fórmula directa en O(1). La solución previa del usuario hacía lo mismo con más ramas; aquí queda en una línea.

## E. Excruciating Elevators

**Enunciado.** Hay 4 ascensores que suben y bajan sin parar entre los pisos 0 y 10^6, y se elige su fase inicial. Hay que visitar n ≤ 35 pisos en orden, trabajando t_i segundos en cada uno, y terminar lo antes posible.

**Solución.** El tiempo total es la suma fija de viajes y trabajos más las esperas. Trabajando módulo P = 2·10^6 (periodo de un ascensor), cada tramo i tiene un instante ideal c_i y cada ascensor una fase k_j; la espera del tramo es (c_i + k_j − W) mod P, con W la espera acumulada. Fijadas las fases, lo óptimo es tomar siempre el ascensor que pase primero. En una solución óptima cada ascensor tiene algún tramo sin espera, lo que obliga a que k_j = k_j' ± (c_{i−1} − c_i) respecto a otro ascensor j'. Se enumeran esas fases como un árbol de profundidad ≤ 3 (unos 800 mil conjuntos distintos) y se simula el greedy con poda (la espera acumulada solo crece). Ojo: anclar cada ascensor en su primer uso NO es óptimo; la enumeración de profundidad 3 coincidió con una fuerza bruta sobre fases en 300 casos aleatorios con periodo pequeño. Python tarda ~8 s con n = 35; C++ 0,6 s.

## F. Fences Make Good Neighbors

**Enunciado.** Hay que triangular un polígono convexo (n ≤ 500) con la menor longitud total de diagonales. No se pueden usar diagonales que pasen por las casas de los dos hermanos, y entre los triángulos de ambos debe haber exactamente un triángulo intermedio.

**Solución.** Para cada cadena a→b del polígono, C[a][b] es el costo mínimo de triangular la región cortada por la diagonal a–b. Sale de la recurrencia clásica sobre el vértice v del triángulo (a,v,b). A1[a][b] y A2[a][b] usan la misma recurrencia, pero exigen que el triángulo (a,v,b) contenga estrictamente al hermano 1 o al 2. Las diagonales que pasan por un hermano valen infinito y los lados del polígono valen 0. Después se prueba cada triángulo central (i,j,k): sus lados separan tres regiones; se asigna el hermano 1 a una, el 2 a otra y la tercera queda libre (6 asignaciones), sumando las diagonales del triángulo. Si nada es válido, −1. Python lento: usar C++ en el juez.

*Rendimiento:* en el peor caso local, C++ tarda 1.2 s o menos; Python tarda entre 5 y 8 s y puede pasarse del límite de tiempo.

## G. Geometry Rush

**Enunciado.** Un punto parte de (0,0) y en cada paso va a (x+1, y±1) sin tocar dos poligonales monótonas en x, un techo y un piso. Se pide la y mínima y máxima alcanzables en x = w, o impossible.

**Solución.** Entre dos curvas monótonas en x la zona libre es un corredor, así que en cada columna las alturas alcanzables forman un intervalo [lo, hi] con la paridad de x. Los vértices tienen coordenadas enteras, de modo que en la franja [x, x+1] cada curva es un segmento recto, más tramos verticales en x y en x+1. Una diagonal es válida si va estrictamente por debajo del techo y por encima del piso en ambos extremos. Por eso se precalculan ceil(mín techo) y floor(máx piso) en cada X entero, interpolando con aritmética entera. Las subidas válidas forman un intervalo de y, y las bajadas también. Se intersectan con [lo, hi], se ajusta la paridad y su unión es el nuevo intervalo. Si queda vacío, impossible.

## H. Honest (or dishonest) Lottery

**Enunciado.** Hay 10n sorteos de 5 números entre 1 y 50. Hay que listar en orden los números que aparecen más de 2n veces, o −1 si no hay ninguno.

**Solución.** Basta un arreglo de 50 contadores. Se leen todos los números de una vez (5 por sorteo, 10n sorteos) y se incrementa el contador de cada uno. Al final se recorren los valores del 1 al 50 y se imprimen, separados por espacio, los que tienen contador > 2n. Si no hay ninguno, se imprime −1. Como el recorrido va en orden, la lista ya sale de menor a mayor y no hace falta ordenar. El tiempo es lineal en la entrada y la memoria, constante. Es una versión más corta de la solución previa del usuario.

## I. Intermill Logistics

**Enunciado.** Hay n molinos; cada uno muele p kg/h y está a t horas de ida y otras t de vuelta. Hay que repartir w kg de trigo para recibirlo todo de vuelta lo antes posible.

**Solución.** Para un tiempo final T, el molino i procesa p_i·max(0, T − 2t_i) kg, y se busca el T mínimo con suma ≥ w. Esa suma es lineal por tramos, así que basta ordenar los molinos por t. Con los k más cercanos, T_k = (w + Σ 2·t_i·p_i) / Σ p_i, y es la respuesta en cuanto T_k ≤ 2·t del siguiente molino, porque ese ya no ayudaría. Todo se hace con enteros exactos (enteros grandes en Python, __int128 en C++, porque 2·t·Σp llega a unos 2·10^23) y solo se divide al imprimir. El costo lo domina el ordenamiento, O(n log n).

## J. Jump ... Triple Jump

**Enunciado.** Se conoce el conjunto de todas las sumas posibles de 3 saltos (con repetición) hechos con tres distancias distintas a < b < c. Hay que recuperar a, b y c.

**Solución.** La menor suma posible es 3a y la mayor es 3c, así que a = d_min/3 y c = d_max/3 salen directo. Para b se prueba cada valor entre a+1 y c−1 (como mucho unos 330). Con cada candidato se generan las 10 sumas de multiconjuntos de tamaño 3 de {a, b, c} y se compara ese conjunto con la lista dada; el primero que coincide es la respuesta. La solución previa del usuario buscaba b con una sola condición, lo que puede dar falsos positivos. Comparar el conjunto completo evita ese riesgo y sigue siendo trivial en tiempo.

## K. Knowing the Clock

**Enunciado.** Dados los ángulos enteros de la aguja horaria (h) y del minutero (m), decidir si corresponden a una hora real.

**Solución.** Si han pasado t minutos desde las 12, la horaria está en t/2 grados y el minutero en 6t mod 360. Como h fija el tiempo exacto, t = 2h minutos, y entonces el minutero tiene que estar en 12h mod 360. La respuesta es yes si y solo si (12·h) mod 360 == m. Con los ejemplos: h=32 da 384 mod 360 = 24, que coincide; h=60 da 0, que no es 90. Todo es aritmética entera, sin flotantes, a diferencia de la solución previa, que comparaba contra m/12 en punto flotante.

## L. Linguistic Labyrinth

**Enunciado.** En una retícula n^3 (n ≤ 22) con letras B, A, P y C, hay que contar las cuaternas B-A-P-C en las que los ángulos BAP y APC son de 90°.

**Solución.** Se fija el vector v = P − A. Las condiciones quedan B·v = A·v (B está en el plano perpendicular a v que pasa por A) y C·v = P·v = A·v + |v|². Para cada v (unos (2n−1)^3 vectores) se buscan los pares (A, P = A+v), y si no hay ninguno se pasa al siguiente. Si hay, se arman histogramas de B·v y de C·v y por cada par se suma cntB[A·v]·cntC[A·v + |v|²]. Los productos escalares están en [−1400, 1400] y caben en un arreglo con desplazamiento. En C++ solo se limpian las casillas usadas y en Python se usan diccionarios como histogramas (Python lento: usar C++ en el juez). El resultado necesita 64 bits.

*Rendimiento:* en el peor caso local, C++ tarda 1.2 s o menos; Python tarda entre 5 y 8 s y puede pasarse del límite de tiempo.

## M. Marching Orders

**Enunciado.** En cada paso se saca de la lista alfabética al profesor de la posición m mod (tamaño restante). Dado el orden final, decidir si algún m < 10^9 lo produce y dar el menor.

**Solución.** Simulando sobre la lista restante, cada paso i fija la congruencia m ≡ r_i (mod n−i), donde r_i es la posición de la letra elegida. Queda un sistema con módulos 20, 19, …, 1, que no son coprimos. Se combina de forma incremental: con la solución actual a (mod M) se busca t en [0, k) tal que a + M·t ≡ r (mod k). Si no existe, la respuesta es NO; si existe, a += M·t y M = mcm(M, k). El a final es el menor no negativo y, como mcm(1..20) = 232792560 < 10^9, siempre cumple la cota. Una fuerza bruta sobre m confirmó los resultados.
