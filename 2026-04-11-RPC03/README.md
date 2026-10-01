# RPC 03 - 2026 (Competitive Programming Network, 3rd Activity)

Fecha: 2026-04-11  
Juez: https://redprogramacioncompetitiva.com/contests/2026/03

Pruebas: `python tools/test.py 2026-04-11-RPC03` (en `tests/` están los ejemplos y casos extra; las fuerzas brutas están en `tests/brute/`).

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | A Little Leftover Pizza | Pizza.py / Pizza.cpp | Implementación / aritmética | O(n) | local-ok |
| B | Andor Strikes Again | Andor.py / Andor.cpp | DP en árboles | O(N) | local-ok |
| C | AROD | AROD.py / AROD.cpp | Conteo / geometría en retícula | O(mx·my + V log V + mx² + my²) | local-ok |
| D | But I Want to Win | Butiwant.py / Butiwant.cpp | Greedy / simulación | O(c log c) | local-ok |
| E | Chess Solitaire | Chess.py / Chess.cpp | Backtracking con memoización | O(estados · m²) | local-ok |
| F | Fractional Sequence | Sequence.py / Sequence.cpp | Matemáticas | O(1) | local-ok |
| G | How Many Balls? | Balls.py / Balls.cpp | Matemáticas / ecuación cuadrática | O(R), R = 10⁶ | local-ok |
| H | Move It, Slowpoke! | Slowpoke.py / Slowpoke.cpp | Dijkstra sobre estados | O(m · d · grado · log) | local-ok |
| I | Number Pyramid | Pyramid.py / Pyramid.cpp | Propagación de restricciones | O(n²) | local-ok |
| J | Polyomino Tiling | Polyomino.py / Polyomino.cpp | Cadenas / palíndromos con hueco + bitsets | O(k³/64) peor caso teórico; ~k²/8 arcos × k/64 en la práctica | local-ok |
| K | Triptych | Triptych.py / Triptych.cpp | DP de conteo | O(w³) | local-ok |
| L | Valley Gulls | Valley.py / Valley.cpp | Simulación por eventos | O(p² · (p + m)) | local-ok |

## A. A Little Leftover Pizza (`Pizza`)

**Enunciado:** Hay pizzas pequeñas (6), medianas (8) y grandes (12 porciones) con sobrantes; se pueden juntar porciones del mismo tamaño en una caja de ese tamaño. Mínimo de cajas.

**Solución:** Como solo se pueden juntar porciones de pizzas del mismo tamaño, cada tamaño se resuelve por separado. Se suman las porciones sobrantes de las pizzas pequeñas, medianas y grandes, y cada tamaño necesita ceil(total/capacidad) cajas, con capacidad 6, 8 y 12. Ninguna caja puede llevar más porciones de las que traía originalmente, y nada impide llenarla hasta esa capacidad, así que redondear la división hacia arriba da exactamente el mínimo. Un tamaño sin porciones aporta cero cajas. La lectura es lineal y la memoria constante: solo se guardan tres acumuladores.

## B. Andor Strikes Again (`Andor`)

**Enunciado:** Árbol AND/OR dado por niveles (los tipos se alternan) con hojas T/F. Mínimo de hojas que hay que cambiar para invertir el valor de la raíz.

**Solución:** Para cada nodo se calculan dos costos: volverlo verdadero (cT) y volverlo falso (cF). En una hoja el costo es 0 para su valor actual y 1 para el otro. En un nodo AND, para que sea verdadero todos los hijos deben serlo (cT = suma de los cT de los hijos) y para que sea falso basta un hijo (cF = mínimo de los cF); en un OR es al revés. El árbol llega por niveles: se guardan las filas y se recorren desde la última hasta la raíz, repartiendo en orden los hijos del nivel de abajo entre los nodos internos. La respuesta es el costo del valor contrario al actual de la raíz, max(cT, cF), porque el valor actual cuesta 0.

## C. AROD (`AROD`)

**Enunciado:** Contar los triángulos agudos, rectos, obtusos y degenerados con vértices en la retícula (0..mx) × (0..my).

**Solución:** Degenerados: entre dos extremos separados por (dx,dy) hay gcd(dx,dy)-1 puntos intermedios; se multiplica por el número de traslaciones. Los demás se agrupan por caja envolvente w×h, que aparece (mx-w+1)(my-h+1) veces, y siempre tienen un vértice en una esquina. (i) Con dos esquinas opuestas, el tercer punto queda dentro del círculo cuyo diámetro es la diagonal: salen 4 rectos y el resto obtusos, descontando la diagonal. (ii-b) Con dos esquinas adyacentes y un punto en el lado opuesto, es obtuso si x(w-x) > h², lo que se cuenta con raíz entera. (ii-a) Con una esquina y un punto en cada lado lejano, el ángulo en B es obtuso si w·x' < y(h-y); esa suma ponderada sale de una criba sobre los productos w·x'. Agudos = total menos el resto. Comprobado contra fuerza bruta.

## D. But I Want to Win (`Butiwant`)

**Enunciado:** Votación con eliminación del menos votado en cada ronda. Si en el mejor caso el segundo recibe todos los votos de los eliminados, ¿cuántas rondas necesita para superar el 50%?

**Solución:** Si el primero ya tiene más de la mitad, gana en la primera ronda y es imposible. En el mejor caso para el segundo, todos los votos de cada eliminado pasan a él. Los demás candidatos no cambian, así que en cada ronda se elimina el menor de los que quedan (los valores son distintos, no hay empates). Se ordenan los votos y se suman los menores al segundo, contando rondas hasta que supere estrictamente la mitad del total. Si solo quedan dos candidatos sin superarla (o empatados), o si había solo dos desde el principio, se imprime IMPOSSIBLE TO WIN.

## E. Chess Solitaire (`Chess`)

**Enunciado:** Tablero n×n con hasta 10 piezas (sin peones) en el que cada movimiento debe capturar. Hay que hallar la secuencia de capturas lexicográficamente menor que deje una sola pieza.

**Solución:** Se hace una búsqueda en profundidad. En cada estado se generan todas las capturas legales: el caballo y el rey saltan, y el alfil, la torre y la dama se deslizan hasta la primera pieza que encuentran. Luego se ordenan por (casilla origen, casilla destino) como texto. Probándolas en ese orden, la primera secuencia completa que aparece es justo la del desempate lexicográfico movimiento a movimiento. Cada captura quita una pieza, así que la profundidad es m-1 <= 9. Los estados (piezas con su posición) que ya se sabe que no tienen solución se guardan en un conjunto para no repetirlos. Si la raíz falla, se imprime No solution.

## F. Fractional Sequence (`Sequence`)

**Enunciado:** La sucesión va por bloques: el bloque i es i, i+1/i, ..., i+(i-1)/i. Dado n <= 4·10⁹, imprimir S(n) como entero o como número mixto reducido.

**Solución:** El bloque i tiene exactamente i términos, así que antes de él hay i(i-1)/2. Se busca el i con i(i-1)/2 < n <= i(i+1)/2 a partir de una raíz cuadrada aproximada, corregida con un par de pasos para evitar errores de redondeo. La posición dentro del bloque es k = n - i(i-1)/2 - 1 y el valor es i + k/i. Si k = 0 se imprime solo i; si no, se reduce k/i dividiendo entre su gcd y se imprime 'i a/b'. Todo cabe en enteros de 64 bits, porque i es del orden de 9·10⁴.

## G. How Many Balls? (`Balls`)

**Enunciado:** P(r,g) = 2rg/((r+g)(r+g-1)). Dado p/q, hallar el menor r <= 10⁶ con g >= r tal que P(r,g) = p/q.

**Solución:** De 2rgq = p(r+g)(r+g-1), despejando g, sale la cuadrática p·g² + (p(2r-1) - 2rq)·g + p(r² - r) = 0. Se recorre r de 1 a 10⁶ en orden, así que el primero que sirve es el de menor r. Para cada r se calcula el discriminante, que debe ser no negativo y cuadrado perfecto (raíz entera exacta: isqrt en Python, sqrtl corregido en C++). La raíz mayor, (-B + raíz)/(2p), tiene que ser entera y al menos r. El enunciado garantiza a lo sumo un g válido por cada r. Los valores intermedios llegan a unos 4·10¹⁸, que cabe en long long.

## H. Move It, Slowpoke! (`Slowpoke`)

**Enunciado:** Grafo con pares ordenados de calles 'continuas': una cadena continua de dos o más calles no puede medir más de d. No se permiten vueltas en U. Camino más corto de s a t.

**Solución:** El estado es la calle dirigida por la que se acaba de llegar (a->b) junto con el largo c del tramo continuo actual, acotado a d+1. Desde (a->b, c) se puede seguir por cualquier calle b->x con x != a, porque no hay vueltas en U. Si (a,b,x) es un par continuo, el tramo pasa a c+l y solo vale si c+l <= d; si no lo es, el tramo se reinicia en l (una calle sola sí puede medir más que d). Dijkstra arranca desde todas las calles que salen de s. Las transiciones no continuas no dependen de c, así que solo se relajan la primera vez que la calle sale de la cola. La respuesta es la primera llegada a t.

## I. Number Pyramid (`Pyramid`)

**Enunciado:** Pirámide en la que cada casilla es la suma de las dos de abajo, con casillas vacías. Decir si la solución es única (y mostrarla), si es ambigua o si no hay solución.

**Solución:** Según el enunciado, las tarjetas válidas se resuelven deduciendo casillas a partir de sus vecinas, así que se simula esa propagación con una cola. En cada triángulo (padre, hijo izquierdo, hijo derecho) se cumple padre = izq + der. Si se conocen dos valores, se calcula el tercero y se encolan los triángulos que tocan la casilla nueva; si se conocen los tres, se comprueba la igualdad. Una contradicción, o un valor deducido fuera de [-99, 99], da no solution. Si al final queda alguna casilla vacía, hay grados de libertad y la respuesta es ambiguous; si no, solvable y se imprime la pirámide. Cada casilla se llena una sola vez: O(n²).

## J. Polyomino Tiling (`Polyomino`)

**Enunciado:** Dada la palabra del borde de un poliominó, contar en todas sus rotaciones las formas de escribirla como X Y X̄ Ȳ o X Y Z X̄ Ȳ Z̄ (X̄ = X al revés con las direcciones invertidas).

**Solución:** En ambas formas, cada factor U que empieza en q tiene su reverso complementado en q+h, con h = k/2. Un arco (q,L) es bueno si B[q..q+L) y B[q+h..q+h+L) son reverso-complemento. Esa condición empareja la posición i con c+h-i, donde c es la suma de los extremos; con c fijo, los arcos buenos están anidados, así que se obtienen expandiendo desde cada uno de los k centros. Una factorización es una cadena de 2 o 3 arcos buenos seguidos que suman exactamente h. Para 3 arcos se fija el primero (q1,a) y, con un AND de bitsets, se cuentan los b para los que (q1+a,b) y el arco que cierra en q1+h son buenos. Cada factorización aparece en las rotaciones s y s+h, de ahí el ×2.

## K. Triptych (`Triptych`)

**Enunciado:** Contar secuencias de A, B y C de largo w sin AA, CC ni BBB, cuyas cantidades de cada letra difieran a lo sumo en d y que no sean palíndromos.

**Solución:** Primero se cuentan todas las secuencias que cumplen las reglas de variedad y equilibrio, y después se restan los palíndromos que también las cumplen. El DP avanza posición a posición con estado (cantidad de A, cantidad de B, último estado entre A, B, BB y C); la cantidad de C sale del largo. Las transiciones prohíben AA, CC y BBB. Al final se suman los estados cuyas tres cantidades difieren a lo sumo en d. Un palíndromo queda fijado por su primera mitad: con w par, la mitad debe terminar en una B sola (el centro queda BB); con w impar, la letra central debe ser distinta de la última de la mitad. Las cantidades totales son el doble de las de la mitad más la del centro. Todo cabe en 64 bits.

## L. Valley Gulls (`Valley`)

**Enunciado:** Terreno lineal a trozos entre dos acantilados, con lluvia de r pies por hora. Para cada nido, decir en qué momento lo alcanza el agua.

**Solución:** El terreno se parte en cuencas separadas por los máximos locales; los acantilados cuentan como altura infinita. Cada lago recibe la lluvia que cae sobre todo su ancho (r·ancho de área por hora) más lo que desbordan los lagos llenos que drenan hacia él. Un lago lleno desborda por su borde más bajo y el agua sigue hasta llegar a un lago que todavía se está llenando. En cada fase se calcula cuánto tarda cada lago en llegar a su borde más bajo. Se avanza hasta el evento más próximo, y ese lago queda lleno o se fusiona con el vecino lleno a la misma altura. Antes de avanzar se revisa si algún nido del lago queda cubierto, usando el área exacta bajo el nivel del nido (trapecios y triángulos).

**Nota sobre J:** en el peor caso (k = 10000, rectángulo de 2500×2500) la versión en Python tarda unos 12 s y la de C++ unos 2 s. Conviene enviar la de C++.

**Nota sobre I:** cuando la propagación se estanca sin contradicción, se responde ambiguous (es la interpretación del enunciado: las tarjetas válidas se resuelven por pasadas).
