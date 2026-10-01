# RPC 11 de 2025 (Competitive Programming Network, 11th Activity)

**Fecha:** 27 de septiembre de 2025

**Juez:** https://redprogramacioncompetitiva.com/contests/2025/11

Soluciones en Python 3 y C++11. Pruebas en `tests/` (ejemplos del enunciado y casos extra `.7`-`.9`); las fuerzas brutas usadas para validar están en `tests/brute/`. Para correrlas: `python tools/test.py 2025-09-27-RPC11`.

Nota: en los problemas con salida real (E, I, M) los `.out` usan el formato que imprime la solución (coincide con el enunciado dentro de la tolerancia 1e-6) porque el comparador local es exacto.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Intentional Blank Page | `Intentional.py` / `Intentional.cpp` | Ad hoc | O(p) | local-ok |
| B | Full House | `Full.py` / `Full.cpp` | Ad hoc, conteo | O(1) | local-ok |
| C | Duck Stress Balls | `Duck.py` / `Duck.cpp` | Greedy, conteo | O(c) | local-ok |
| D | Twin Numbers | `Twin.py` / `Twin.cpp` | Matemáticas, conteo por dígitos | O(len) | local-ok |
| E | Simple House | `Simple.py` / `Simple.cpp` | Geometría, búsqueda ternaria | O(I^2), I = 100 iteraciones | local-ok |
| F | Pathfinder and Wolves | `Pathfinder.py` / `Pathfinder.cpp` | BFS multifuente, DSU (cuello de botella) | O(r*c*α) | local-ok |
| G | Festival of Blossoms | `Festival.py` / `Festival.cpp` | Combinatoria sobre cadenas (bordes, Guibas-Odlyzko) | O(N * bordes(S)) | local-ok |
| H | Birthday Bash | `Birthday.py` / `Birthday.cpp` | Probabilidad (coleccionista de cupones), tabla precalculada | O(10^6) | local-ok |
| I | Dark Things | `Dark.py` / `Dark.cpp` | Geometría, búsqueda binaria | O(k * I * n), I = 55 | local-ok |
| J | Galactic Voyage | `Galactic.py` / `Galactic.cpp` | Dijkstra sobre residuos, CRT | O(m * (S + P^2 K) log m) | local-ok |
| K | Degenerating Walkways | `Degenerating.py` / `Degenerating.cpp` | Probabilidad en árboles, árbol virtual, rerooting | O((n + m) log n) | local-ok |
| L | Copogonia | `Copogonia.py` / `Copogonia.cpp` | Grafos, fuerza bruta sobre subconjuntos | O(2^k * n^2) | local-ok |
| M | Weekend Gardening | `Weekend.py` / `Weekend.cpp` | Probabilidad, DP | O(c*n*e) | local-ok |

## A. Intentional Blank Page

**Resumen:** Dados p problemas y sus páginas, contar cuántas páginas quedan en blanco al imprimir a doble cara sin empezar un problema en una página trasera.

**Solución:** Cada problema empieza en una página frontal. Si tiene un número par de páginas termina en una trasera y el siguiente arranca de frente sin desperdicio; si tiene un número impar, su última página queda en el frente y la trasera correspondiente se deja en blanco con el mensaje. Por lo tanto la respuesta es simplemente la cantidad de problemas con número impar de páginas. Se lee la lista y se suma x mod 2 de cada valor. No hay casos especiales: incluso el último problema cuenta si es impar, como muestra el tercer ejemplo con un solo problema de una página.

## B. Full House

**Resumen:** Dado un entero de cinco dígitos, decidir si es un full house: tres dígitos de un valor y dos de otro.

**Solución:** Se cuentan las apariciones de cada dígito del número tratado como cadena. Un full house corresponde exactamente a que las frecuencias, ordenadas de menor a mayor, sean [2, 3]: dos valores distintos, uno repetido dos veces y otro tres. Cualquier otra distribución falla: cinco iguales da [5], cuatro y uno da [1, 4], tres y dos distintos da [1, 1, 3], etc. Con un Counter en Python o un map en C++ se obtienen las frecuencias, se ordenan y se comparan contra la lista objetivo. Es O(1) porque siempre hay cinco dígitos.

## C. Duck Stress Balls

**Resumen:** Hay 3n patos de c colores; cada uno de los n equipos debe recibir tres patos de colores distintos. Decidir si es posible.

**Solución:** Cada equipo puede recibir a lo sumo un pato de cada color, así que un color con más de n patos hace imposible el reparto. Esa condición también es suficiente: repartiendo siempre un pato de cada uno de los tres colores más abundantes se mantiene la invariante máximo <= equipos restantes (argumento clásico de intercambio) hasta agotar todo. Por eso basta verificar 3*max <= total. Se validó contra una simulación greedy en casos aleatorios. El segundo ejemplo falla porque 59 y 60 superan los 40 equipos.

## D. Twin Numbers

**Resumen:** Contar, módulo 10007, los números twin (dígitos en pares iguales: 88, 775588) en un rango con límites de hasta 100000 dígitos.

**Solución:** Un twin de 2m dígitos queda determinado por su mitad h de m dígitos sin cero inicial. Se define f(X) = twins <= X. Los de menor longitud suman 9*(1+10+...+10^(t-1)) = 10^t - 1, con t la mitad de la mayor longitud par menor que la de X. Si X tiene longitud impar no hay más. Si es par, se recorren los pares de X: mientras ambos dígitos coinciden se copian en h; en el primer par distinto (a, b) se toma a si a < b o a-1 si a > b y se completa con nueves. Todo se lleva mod 10007. La respuesta es f(hi) - f(lo) + [lo es twin].

## E. Simple House

**Resumen:** Dentro de un terreno rectangular rotado, ubicar la casa rectangular alineada a los ejes con proporción w:h de máxima área.

**Solución:** La casa es un rectángulo de lados w*t y h*t con centro (x, y). Un rectángulo alineado cabe en un polígono convexo si sus cuatro esquinas cumplen cada semiplano; para el lado con normal (a, b) eso equivale a a*x + b*y + t*(|a|w + |b|h)/2 <= c. Fijado el centro, el mayor t es el mínimo de cuatro funciones lineales, que es cóncavo en (x, y). Por eso se hace búsqueda ternaria anidada: en x por fuera y en y por dentro, 100 iteraciones cada una. La orientación de cada semiplano se fija usando el centroide de los vértices. El área es w*h*t^2.

## F. Pathfinder and Wolves

**Resumen:** En una grilla con lobos, ir de (1,1) a (r,c) maximizando la mínima distancia (en pasos) a un lobo a lo largo del camino.

**Solución:** Primero un BFS multifuente desde todos los lobos da la distancia de cada celda al lobo más cercano; la cola del BFS queda ordenada por distancia. Luego se resuelve un problema de camino de cuello de botella máximo: se activan las celdas de mayor a menor distancia (recorriendo la cola al revés) y se unen con sus vecinas ya activas en un DSU. La primera vez que (1,1) y (r,c) quedan en la misma componente, la distancia de la celda recién activada es la respuesta, porque existe un camino que solo usa celdas con al menos esa distancia. Las celdas con lobo nunca se activan.

## G. Festival of Blossoms

**Resumen:** Contar cadenas de longitud N sobre K letras que contienen a S como substring, módulo 1e9+7.

**Solución:** Se cuentan las que no contienen S y se restan de K^N. Sea a[n] el número de cadenas de largo n sin S y b[n] las que tienen su primera aparición de S terminando justo en n. Extender una cadena sin S con una letra da K*a[n-1] = a[n] + b[n]. Pegar S al final de una cadena sin S de largo n-m produce una primera aparición que termina en n-m+j para algún borde j de S (prefijo igual a sufijo, incluido j = m), y el resto queda forzado: a[n-m] = suma de b[n-m+j]. Eso da b[n] y luego a[n]. Los bordes se calculan directamente (m <= 1000).

## H. Birthday Bash

**Resumen:** Esperanza del número de personas hasta cubrir los n cumpleaños posibles, con n hasta 2e9, módulo 1e9+7.

**Solución:** Es el problema del coleccionista de cupones: E = n * H_n con H_n = 1 + 1/2 + ... + 1/n. Como n llega a 2e9 no se puede sumar en tiempo de ejecución, así que se precalculó offline (en C++, unos segundos) el valor H_{i*10^6} mod p para i = 0..1000 y se incrustó como tabla en el código. En ejecución se suman los menos de 10^6 términos restantes como una sola fracción num/den (num = num*k + den, den = den*k) para usar un único inverso modular. Para n > p se usa 1/k = 1/(k-p) y H_{p-1} = 0 (Wolstenholme); n = p da 1.

## I. Dark Things

**Resumen:** Dividir un sector circular de radio R y ángulo [-theta, theta], quitando círculos interiores disjuntos, en k partes de igual área mediante rayos desde el origen.

**Solución:** Sea A(psi) el área libre con ángulo entre -theta y psi: R^2/2*(psi+theta) menos la parte de cada círculo que queda del lado de ángulo menor que psi. Como ningún círculo contiene el origen y todo cabe en menos de 180 grados, esa parte es un segmento circular respecto a la recta por el origen con ángulo psi: con distancia con signo t = r*sin(phi - psi), el área es rho^2*acos(t/rho) - t*sqrt(rho^2 - t^2), recortando t a [-rho, rho]. Los círculos que no cruzan el rayo (intervalo angular phi ± asin(rho/r)) se resuelven sin trigonometría. A es creciente, así que cada ángulo de área j*Total/k se halla por bisección.

## J. Galactic Voyage

**Resumen:** Desde 0 se avanza con pasos s_i o con saltos de agujero de gusano (de múltiplo de p_j a múltiplo de p_k a distancia <= K). Hallar la mayor posición inalcanzable.

**Solución:** Con m = min(s), si x es alcanzable también lo es x + t*m, así que basta d[r] = menor posición alcanzable con residuo r mod m (idea de Frobenius). Aristas: sumar cualquier s_i, y saltos: desde x = 0 (mod p_j) hasta x+delta = 0 (mod p_k), delta <= K. Para un residuo r con distancia d, el menor x >= d con x = r (mod m) y esas dos congruencias se obtiene por CRT; las combinaciones (j, k, delta) se precalculan. Como el costo resultante es monótono en d, Dijkstra es válido. Si algún residuo queda inalcanzable hay infinitos (respuesta -1); si no, la respuesta es max(d) - m, o -1 si es <= 0.

## K. Degenerating Walkways

**Resumen:** Caminata aleatoria sin repetir aristas en un árbol desde un hub uniforme; se recolectan estrellas siguiendo una secuencia objetivo y en cada paso el portal funciona con probabilidad 1-(p/q)^(t+1). Esperanza de la estabilidad final.

**Solución:** Por linealidad, la respuesta es la suma de las probabilidades de recolectar en cada nodo b; si x_{L+1} está en b (pos L), hay que llegar a b con nivel L. Esa masa viene de nodos con pos L-1 (o de los inicios, para L = 0) por caminos sin otros nodos de pos L, y cada nodo intermedio multiplica por (p/q)^(L+1)/(deg-1). Para cada nivel se construye el árbol virtual de A_{L-1} U A_L (aristas comprimidas con prefijos de 1/(deg-1)) y se pasan mensajes de subida y bajada; los nodos de A_L absorben. Se guarda la masa por dirección de llegada para no emitirla de vuelta por la misma arista en el siguiente nivel.

## L. Copogonia

**Resumen:** Un polígono convexo de n ciudades; elegir el subconjunto de a lo sumo k nuevas vías de mínimo costo para que toda distancia de camino mínimo sea <= m.

**Solución:** Con k <= 10 hay solo 1024 subconjuntos. Se hace DFS decidiendo incluir o no cada vía; al incluir la vía (u, v) de longitud euclidiana w, la matriz de distancias se actualiza en O(n^2) con d[i][j] = min(d[i][j], d[i][u] + w + d[v][j], d[i][v] + w + d[u][j]), que es exacto al agregar una sola arista. La matriz inicial sale de las distancias sobre el ciclo (perímetro acumulado, el menor de los dos sentidos). Se poda cuando el costo ya no mejora la mejor respuesta, y se corta la rama en cuanto el máximo de la matriz es <= m, porque agregar más vías solo cuesta más.

## M. Weekend Gardening

**Resumen:** Se compran plantas una a una al azar entre tres tipos de costo distinto; se para al alcanzar al menos L. Probabilidad de terminar con total entre L y H.

**Solución:** El estado es (i, j, l): cuántas baratas, normales y caras se han comprado; con eso se conoce el total y las plantas restantes. Desde un estado con total < L, cada tipo se elige con probabilidad (restantes de ese tipo)/(restantes totales). Si la compra lleva el total a >= L se para: suma a la respuesta si no pasa de H. Si se acaban las plantas sin llegar a L es fracaso. Hay a lo sumo 101^3 estados y se recorren por número de plantas compradas (Python) o en orden lexicográfico (C++), que respeta las transiciones. Se validó contra una recursión exhaustiva.
