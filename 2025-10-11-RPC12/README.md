# RPC 12 - 2025 (Competitive Programming Network, 12th Activity)

Fecha: 2025-10-11

Juez: https://redprogramacioncompetitiva.com/contests/2025/12

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Alto Adaptation | Adaptation.py / Adaptation.cpp | DP | O(n^2) | local-ok |
| B | Bottle of New Port | Bottle.py / Bottle.cpp | Matemáticas / ad hoc | O(1) | local-ok |
| C | Chess | Chess.py / Chess.cpp | Simulación | O(N^2 + M) | local-ok |
| D | Dralinpome | Dralinpome.py / Dralinpome.cpp | Strings / conteo | O(|s|) | local-ok |
| E | Encrypting | Encrypting.py / Encrypting.cpp | Strings / ad hoc | O(N) | local-ok |
| F | Flakes | Flakes.py / Flakes.cpp | Simulación / grillas | O(nm(n+m)) | local-ok |
| G | Genealogy Gumbo | Genealogy.py / Genealogy.cpp | Grafos / alcanzabilidad | O(n log n) | local-ok |
| H | Hidden Sequence | Hidden.py / Hidden.cpp | Greedy / punteros | O(total) | local-ok |
| I | Item Selection | Item.py / Item.cpp | Greedy | O(n) | local-ok |
| J | Judge Meetings | Judge.py / Judge.cpp | Simulación | O(n*m) | local-ok |
| K | Koehandel | Koehandel.py / Koehandel.cpp | Ad hoc | O(1) | local-ok |
| L | Luminosity | Luminosity.py / Luminosity.cpp | DP de intervalos / TSP en la recta | O(K^2), K <= 2N+1 | local-ok (py lento: usar C++) |
| M | Most Scenic Cycle | Most.py / Most.cpp | Grafos serie-paralelo | O(E log E) | local-ok |

Pruebas: `python tools/test.py 2025-10-11-RPC12`. La fuerza bruta aleatoria (A, G, L, M) está en `tests/brute/stress.py` y los casos grandes se generan con `tests/brute/gen_big.py`.

## A. Alto Adaptation (`Adaptation`)

**Enunciado.** Hay que partir la canción en tramos y transponer cada tramo un número entero de octavas para que todas sus notas queden dentro de [l, h]. Se busca maximizar la longitud del tramo más corto.

**Solución.** Cada nota a admite un rango de octavas k con l <= a+12k <= h: desde ceil((l-a)/12) hasta floor((h-a)/12). Un tramo de notas consecutivas puede cantarse con la misma transposición si la intersección de sus rangos no es vacía. Se hace DP: dp[i] es el mayor valor posible del tramo más corto al partir las primeras i notas (dp[0] = infinito). Para cada i se recorre j hacia atrás manteniendo el máximo de los límites inferiores y el mínimo de los superiores; si la intersección se vacía se corta, y si no, dp[i] = max(dp[i], min(dp[j], i-j)). Con n <= 1000 son a lo sumo medio millón de pasos. La respuesta es dp[n].

## B. Bottle of New Port (`Bottle`)

**Enunciado.** La botella tiene a de alcohol y o de otros líquidos, que se evaporan a ritmos fijos por día. Se pide el porcentaje de alcohol después de d días.

**Solución.** Tras d días el volumen de alcohol es a - d*da y el de otros líquidos o - d*do, pero ninguno puede ser negativo: si un líquido se evapora por completo queda en cero. Se calculan ambos con enteros de 64 bits (d*da llega a 1e18, cabe en long long) y se recorta con max(0, .). El enunciado garantiza que la botella no queda vacía, así que el denominador es positivo. El porcentaje es 100*A/(A+O), que se imprime con 10 decimales. El juez acepta error 1e-6, por lo que la salida no tiene que coincidir carácter a carácter con la de los ejemplos (14.2857142857143 frente a 14.2857142857).

## C. Chess (`Chess`)

**Enunciado.** En un tablero N x N hay M piezas (caballo, torre, reina) que atacan a través de las otras piezas y también su propia casilla. Se pide contar las casillas atacadas.

**Solución.** En vez de pintar cada ataque (una reina ataca O(N) casillas y puede haber N^2 piezas) se marcan líneas: las torres y reinas marcan su fila y su columna, y las reinas también sus dos diagonales, identificadas por r-c y r+c. Los caballos marcan directamente su propia casilla y las hasta 8 casillas a salto de caballo. Luego se recorre el tablero N x N y una casilla cuenta como atacada si está marcada su fila, su columna o alguna de sus diagonales, o si la marcó un caballo. Cada pieza se ataca a sí misma, y eso ya queda cubierto. Total O(N^2 + M).

## D. Dralinpome (`Dralinpome`)

**Enunciado.** Hay que decidir si las letras de una palabra pueden reordenarse para formar un palíndromo.

**Solución.** Una palabra puede reordenarse en un palíndromo si y solo si a lo sumo una letra aparece un número impar de veces: en un palíndromo las letras se emparejan simétricamente alrededor del centro y solo el carácter central (si la longitud es impar) puede quedar sin pareja. Se cuentan las apariciones de cada una de las 26 letras, se cuenta cuántas tienen frecuencia impar y se responde yes si ese número es 0 o 1, y no en otro caso. Es lineal en la longitud de la palabra y usa memoria constante.

## E. Encrypting (`Encrypting`)

**Enunciado.** Un mensaje de 2 filas dibuja letras 'v' (4 columnas) y 'w' (8 columnas) separadas por una columna de puntos. Hay que decodificarlo.

**Solución.** Las letras se separan por exactamente una columna vacía (solo puntos en ambas filas) y dentro de una letra nunca hay columnas vacías: la 'v' ocupa 4 columnas y la 'w' 8. Basta recorrer las columnas de izquierda a derecha contando la longitud de cada racha de columnas no vacías. Al encontrar una columna vacía (o el final) se cierra la racha y se emite 'v' si mide 4 o 'w' si mide 8. Se usa un centinela en la posición N para cerrar la última letra. Las filas se leen como tokens porque no contienen espacios.

## F. Flakes (`Flakes`)

**Enunciado.** En una grilla hay copos de nieve: un '+' con rayas en las 8 direcciones. El tamaño de un copo es su racha más corta. Se pide el copo más grande.

**Solución.** El tamaño de un copo centrado en un '+' es el mínimo, sobre las 8 direcciones, de la racha de caracteres correctos que sale del centro: '|' arriba y abajo, '-' a izquierda y derecha, '\' en la diagonal superior izquierda/inferior derecha y '/' en la otra. Para cada '+' de la grilla se camina en cada dirección mientras el carácter coincida y se toma el mínimo de las 8 longitudes. La respuesta es el máximo sobre todos los centros (0 si no hay '+'). Con n, m <= 50 la fuerza bruta es inmediata. Ojo: el PDF muestra el guion como un carácter largo, pero en la entrada es '-'.

## G. Genealogy Gumbo (`Genealogy`)

**Enunciado.** Hay n relaciones 'A, son of B', y varias personas pueden compartir nombre. Se pregunta si existe un árbol genealógico con una sola raíz que use solo esas personas.

**Solución.** Como varias personas pueden compartir nombre, cada línea es un hijo distinto, y su padre puede ser cualquier persona con ese nombre o una persona sin padre registrado. Solo puede haber una persona sin padre: la raíz. Se arma el grafo de nombres padre -> hijo. Si hay dos o más nombres que son padres pero nunca hijos, es imposible. Si hay uno, ese es la raíz; si no hay ninguno, la raíz es una persona nueva con algún nombre. Es posible si y solo si desde la raíz se alcanzan todos los nombres. Sin candidato, se toma el último vértice en terminar un DFS completo: si alguno alcanza a todos, es ese.

## H. Hidden Sequence (`Hidden`)

**Enunciado.** Cada uno de los 3 jugadores anota la secuencia de ganadores sin incluirse a sí mismo. Hay que reconstruir la secuencia completa, que es única.

**Solución.** La lista del jugador i contiene la secuencia real sin las victorias de i. Si el siguiente ganador real es w, su número debe estar al frente de las dos listas en las que aparece (las de los otros dos jugadores). Dos jugadores distintos no pueden cumplir esto a la vez, porque ambos aparecen en la lista del tercero y solo uno puede estar al frente. Se mantiene un puntero por lista y en cada paso se busca el único w que cumple la condición, se avanza en esas dos listas y se agrega w. La longitud total es la suma de las tres longitudes dividida entre 2.

## I. Item Selection (`Item`)

**Enunciado.** Una web muestra items paginados, con casillas, Select All, Deselect All y botones Siguiente/Anterior. Se pide el mínimo de clics para pasar de la selección previa a la deseada.

**Solución.** Los clics de selección de cada página son independientes. En cada página con diferencias se elige lo más barato: alternar cada casilla distinta, pulsar Select All y desmarcar los no deseados (1 + no deseados de la página), o pulsar Deselect All y marcar los deseados (1 + deseados). Las páginas sin diferencias no cuestan nada y no hace falta visitarlas. Para navegar, sean L y R la primera y la última página con trabajo: hay que recorrer [L, R] partiendo de s, y lo óptimo es ir primero al extremo más cercano, con costo (R-L) + min(|s-L|, |s-R|). Si ninguna página tiene trabajo, la respuesta es 0.

## J. Judge Meetings (`Judge`)

**Enunciado.** Hay n jueces con sus vacaciones dentro de m días. Se pide contar los días en que al menos 3 jueces están disponibles.

**Solución.** Con a lo sumo 10 jueces, 10 vacaciones cada uno y 120 días, alcanza con simular. Se empieza con libres[d] = n para cada día y, por cada vacación [s, e] de cada juez, se resta uno a cada día del intervalo. Como las vacaciones de un mismo juez no se solapan, ningún día se descuenta dos veces para el mismo juez. Al final se cuentan los días entre 1 y m con al menos 3 jueces libres. Que las vacaciones vengan desordenadas no importa, porque cada intervalo se procesa por separado. El trabajo total está acotado por n*10*m, que es muy pequeño.

## K. Koehandel (`Koehandel`)

**Enunciado.** MacDonald apuesta c monedas y tú tienes n. Las apuestas se intercambian y quien apostó más gana una vaca. Hay que elegir la apuesta que maximiza primero las vacas y después las monedas.

**Solución.** Si se apuesta x, se termina con n - x + c monedas, y la vaca la gana quien apostó más. Lo primero es la vaca. Si n > c, se apuesta el mínimo que gana, c+1, y se termina con n-1 monedas. Si n == c no se puede ganar, pero empatando con x = c no se pierde la vaca y se conservan las n monedas. Si n < c la vaca se pierde de todos modos, así que conviene apostar 0 y quedarse con n + c monedas. Son tres casos en O(1). Con valores hasta 1e9, c+1 cabe en 32 bits, pero se usa long long por seguridad.

## L. Luminosity (`Luminosity`)

**Enunciado.** Un guardián parte de 0 a velocidad 1 y debe apagar todos los cristales de los rangos [l, r], cada uno no antes de su tiempo t. Se pide el tiempo mínimo para terminar.

**Solución.** Cada cristal x de la unión debe tocarse por última vez en un tiempo >= R(x), el mayor t entre los rangos que lo contienen. Si se invierte el tiempo, las últimas visitas pasan a ser primeras visitas con plazo, y lo ya visitado es un intervalo que crece alrededor del punto final. Por eso solo importan las coordenadas l_i y r_i: los puntos interiores tienen R menor o igual y se alcanzan antes. R se calcula con un barrido y un heap. Hacia adelante, los pendientes forman un intervalo [i..j] y el guardián está junto a uno de sus extremos; se atiende el extremo izquierdo o el derecho con tiempo max(llegada, R). La DP recorre el intervalo por longitud. RIESGO: la versión Python (pura, sin numpy) tarda ~28 s con N=5000; usar C++ en el juez (~0.7 s).

## M. Most Scenic Cycle (`Most`)

**Enunciado.** El grafo es 2-conexo y sus ciclos regionales forman un árbol, así que es serie-paralelo. Se pide el ciclo simple de al menos 2 aristas con la mayor suma de pesos.

**Solución.** Las condiciones (2-conexo, con E-V+1 ciclos que forman un árbol) describen un grafo serie-paralelo, parecido a uno outerplanar. Se reduce el grafo: las aristas paralelas se fusionan y los vértices de grado 2 se eliminan uniendo en serie sus dos aristas. Cada arista compuesta u-v guarda P, el mejor camino simple de u a v dentro de lo que representa, y C, el mejor ciclo dentro de ella. En serie: P = P1+P2 y C = max(C1, C2). En paralelo: P = max(P1, P2) y C = max(C1, C2, P1+P2), porque el ciclo usa un camino de cada lado. La respuesta es el mayor C. Se validó contra fuerza bruta.
