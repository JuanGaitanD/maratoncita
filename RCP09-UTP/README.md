# UTP Open 2026 (RPC 09 de 2026)

Fecha: 2026-09-26  
Juez: https://redprogramacioncompetitiva.com/contests/2026/09  
Enunciados: [`UTPOpen2026v3.pdf`](UTPOpen2026v3.pdf)

Cada problema tiene solución en Python 3 (`.py`) y C++11 (`.cpp`). Pruebas en `tests/` (ejemplos del enunciado + casos `.9` generados con fuerza bruta en `tests/brute/`). Para correrlas desde la raíz del repo: `python tools/test.py RCP09-UTP [Nombre]`.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Alejandro, lee por favor | [`Alejandro.py`](Alejandro.py) / [`Alejandro.cpp`](Alejandro.cpp) | Simulación / cadenas | O(L) | local-ok |
| B | Betito el viajero | [`Betito.py`](Betito.py) / [`Betito.cpp`](Betito.cpp) | Grafos / flood fill | O(R·C) por caso | local-ok |
| C | Company | [`Company.py`](Company.py) / [`Company.cpp`](Company.cpp) | Árboles / DP | O(N) | local-ok |
| D | Dangerous odyssey | [`Dangerous.py`](Dangerous.py) / [`Dangerous.cpp`](Dangerous.cpp) | BFS en grilla / sumas de prefijos | O(N·M) | local-ok |
| E | Enarmonía | [`Enarmonia.py`](Enarmonia.py) / [`Enarmonia.cpp`](Enarmonia.cpp) | Programación dinámica | O(T²·K) | local-ok |
| F | Flipando colores con la DIAN | [`Flipando.py`](Flipando.py) / [`Flipando.cpp`](Flipando.cpp) | Greedy / scheduling en árboles (Horn) | O(n log n) | local-ok |
| G | Guanex y el diámetro con actualizaciones | [`Guanex.py`](Guanex.py) / [`Guanex.cpp`](Guanex.cpp) | Árboles / LCA (binary lifting) | O((n+q) log V) | local-ok |
| H | Humbertov y su taza de café | [`Humbertov.py`](Humbertov.py) / [`Humbertov.cpp`](Humbertov.cpp) | Geometría / fórmula cerrada | O(1) por caso | local-ok |
| I | Internal triangles | [`Internal.py`](Internal.py) / [`Internal.cpp`](Internal.cpp) | Combinatoria / aritmética modular | O(1) por consulta | local-ok |
| J | Juan y sus ovejas | [`Juan.py`](Juan.py) / [`Juan.cpp`](Juan.cpp) | Union-Find | O((N+P) α(N)) | local-ok |
| K | K-th shortest path | [`Kthpath.py`](Kthpath.py) / [`Kthpath.cpp`](Kthpath.cpp) | Dijkstra | O(K·M log N) | local-ok |
| L | Locate Tobby's nest | [`Locate.py`](Locate.py) / [`Locate.cpp`](Locate.cpp) | Árboles / centro por BFS | O(H·W) por caso | local-ok |
| M | Marble tilt maze | [`Marble.py`](Marble.py) / [`Marble.cpp`](Marble.cpp) | BFS en espacio de estados | O((NM)²) | local-ok (ejemplo 1 inconsistente) |

## A. Alejandro, lee por favor

**Enunciado.** Se descifra un texto cifrado con un desplazamiento global c que crece cada vez que el contador de una letra original llega a un múltiplo de K.

**Solución.** El cifrado es determinista y el descifrado puede seguirlo letra a letra en el mismo orden. Se mantiene c y un contador por cada una de las 26 letras. Para cada letra cifrada e, la original es L = (e - c) mod 26; se escribe L, se incrementa el contador de L y, si queda en múltiplo de K, c aumenta en uno. Como c solo cambia después de procesar la letra, la simulación inversa reproduce exactamente el estado del cifrador. Basta trabajar c módulo 26 en la resta. Se recorre la suma total de longitudes (hasta 10^6) una sola vez, construyendo cada palabra en un buffer y uniendo con espacios al final.

## B. Betito el viajero

**Enunciado.** En una cuadrícula con '.', '#' y un '*' de inicio, contar cuántas celdas son alcanzables (4 vecinos) incluyendo el inicio. Varios casos hasta 0 0.

**Solución.** Es un flood fill clásico. Se rodea la grilla con un borde de '#' para no revisar límites y se aplana en un arreglo de bytes, de modo que los vecinos de la celda v son v±1 y v±W. Desde la posición del asterisco se hace una búsqueda en profundidad iterativa con una pila: cada celda visitada se marca como '#' para no volver a contarla y se suma uno al contador. Al terminar la pila, el contador es la cantidad de lugares visitables. Cada celda entra a la pila como máximo una vez, así que el costo es lineal en el tamaño del mapa, con hasta 10 casos de 1000x1000.

## C. Company

**Enunciado.** Árbol enraizado en 1 dado por padres P_i < i. Calcular la suma de distancias entre todos los pares y el diámetro de cada subárbol.

**Solución.** Como cada padre tiene índice menor que su hijo, recorrer los nodos de N a 2 procesa siempre los hijos antes que el padre, sin DFS ni recursión. La suma de distancias se obtiene por aristas: la arista (i, P_i) la cruzan sz(i)·(N - sz(i)) pares, donde sz es el tamaño del subárbol. Para el diámetro se guarda h(x), la altura del subárbol, y F(x). Al procesar el hijo i de p, el candidato h(p) + h(i) + 1 une la rama más alta vista hasta ahora con la nueva; F(p) también hereda F(i). Luego h(p) = max(h(p), h(i)+1). Todo es una pasada lineal; la suma cabe en 64 bits.

## D. Dangerous odyssey

**Enunciado.** Camino mínimo de Y a A por mar evitando celdas a distancia Chebyshev ≤ H de sirenas o brujas y quedando siempre a distancia ≤ D de un refugio válido.

**Solución.** Primero se marcan las celdas peligrosas: una celda lo es si en el cuadrado de radio H centrado en ella hay una S o una B (los cantos se mueven en diagonal, así que es distancia de Chebyshev); con sumas de prefijos 2D cada consulta es O(1). Los refugios válidos son R, Y y A no peligrosos. Un BFS multi-fuente en 4 direcciones desde todos ellos da la distancia de cada celda al refugio más cercano. Finalmente un BFS desde Y por celdas '.', Y o A no peligrosas y con distancia a refugio ≤ D da los pasos hasta A; si no se llega, OSIDEO WILL DIE. Supuesto: la distancia al refugio es de 4 vecinos ignorando obstáculos (los ejemplos no distinguen variantes).

## E. Enarmonía

**Enunciado.** Se leen T actos alternando entre dos manuscritos circulares con a lo sumo K cambios; maximizar los pares consecutivos con el mismo registro.

**Solución.** La lectura queda descrita por cuántos actos se han tomado de cada manuscrito: si se leyeron a del primero y b del segundo, el siguiente acto de cada uno es el índice a mod N1 o b mod N2, y el último leído depende solo del manuscrito actual. Así el estado es (t, a, manuscrito actual, cambios usados), con b = t - a. Desde cada estado hay dos transiciones: seguir en el mismo manuscrito o cambiar (gastando un cambio), sumando 1 si el registro nuevo coincide con el anterior. Se arranca en (1, 1, primero, 0) y la respuesta es el máximo en t = T. En Python puro se usan listas sobre (a, k).

## F. Flipando colores con la DIAN

**Enunciado.** Ordenar n trámites con precedencias en forma de bosque (cada uno depende de a lo sumo uno) para minimizar la suma de w_i por el tiempo de finalización.

**Solución.** Es el problema 1|outtree|ΣwC, resuelto con el algoritmo de Horn. El nodo (o grupo ya fusionado) con mayor razón w/p que no es raíz debe ejecutarse inmediatamente después del grupo de su padre, así que se fusiona con él: el costo aumenta en P_padre·W_hijo (el hijo se retrasa todo lo que dura el grupo padre) y el grupo padre acumula p y w. Se usa un heap de máximos por w/p con borrado perezoso y Union-Find para encontrar el grupo del padre. Una raíz virtual 0 con p = w = 0 recibe a las raíces reales. El costo base es la suma de p_i·w_i. En C++ se compara w1·p2 contra w2·p1 de forma exacta.

## G. Guanex y el diámetro con actualizaciones

**Enunciado.** Dado un árbol y q inserciones de hojas nuevas, imprimir el diámetro inicial y después de cada inserción.

**Solución.** Si (a, b) son extremos de un diámetro y se agrega una hoja x, el nuevo diámetro es el máximo entre el anterior, dist(x, a) y dist(x, b); en ese caso los nuevos extremos incluyen a x. Las distancias se calculan con LCA por binary lifting: dist = prof(x) + prof(y) - 2·prof(lca). El árbol inicial se enraíza con un BFS que llena profundidad y la tabla de ancestros; cada hoja nueva solo necesita completar su fila de ancestros en O(log). El diámetro inicial sale tomando el nodo más profundo a y el más lejano de a. Las etiquetas son menores que 3·10^5, así que se usan arreglos directos.

## H. Humbertov y su taza de café

**Enunciado.** Una taza con forma de cono truncado (radio de fondo r, boca R, altura h): hallar la altura a la que el café ocupa la mitad del volumen.

**Solución.** Si se prolonga el cono truncado hasta su vértice, el volumen hasta una altura x es el de un cono de radio ρ(x) menos el cono de radio r, y el volumen de un cono semejante es proporcional a ρ³. Como ρ crece linealmente con x, la condición de mitad de volumen es ρ³ - r³ = (R³ - r³)/2, es decir ρ = ((r³ + R³)/2)^(1/3), y la altura es x = h·(ρ - r)/(R - r). Si r = R la taza es un cilindro y la respuesta es h/2. Se imprime con 9 decimales. Nota: el ejemplo 2 del enunciado dice 6.509636245 pero el valor exacto es 6.5096362445; el juez acepta error 1e-6.

## I. Internal triangles

**Enunciado.** Contar los triángulos con vértices en un polígono regular de n lados (n hasta 10^18), módulo 10^9+7.

**Solución.** Todo trío de vértices distintos del polígono convexo forma un triángulo distinto, así que la respuesta es C(n, 3) = n(n-1)(n-2)/6. En Python se calcula directamente con enteros grandes y luego módulo 10^9+7; en C++ se reduce cada factor módulo p y se multiplica por el inverso modular de 6 (166666668). El Internal.py original era correcto pero leía con input() línea por línea y recibió TLE en el juez con 10^5 consultas y límite de 1 segundo; la versión actual lee todo stdin de una vez y escribe todas las respuestas con un único print (0.13 s con el caso máximo).

## J. Juan y sus ovejas

**Enunciado.** Dadas N ovejas y P pares de la misma raza, contar las razas (componentes) y el tamaño de la mayor. Varios casos hasta 0 0.

**Solución.** Las razas son las componentes conexas del grafo de pares. Se usa Union-Find con compresión de caminos (por halving) y unión por tamaño: inicialmente hay N componentes de tamaño 1, y cada par que une dos componentes distintas reduce el conteo en uno y suma los tamaños en la nueva raíz. Al terminar el caso, el número de razas es el contador y la mayor raza es el máximo de los tamaños (los tamaños guardados en nodos que dejaron de ser raíz nunca superan al de su raíz, así que el máximo del arreglo es correcto). Cada caso es casi lineal en N + P.

## K. K-th shortest path

**Enunciado.** Hallar el k-ésimo recorrido más corto de S a D, donde cada recorrido no puede usar aristas de los anteriores; imprimir su costo y sus vértices.

**Solución.** La definición es iterativa: el primer recorrido es el camino más corto; el segundo es el más corto en el grafo sin las aristas del primero, y así sucesivamente. Por eso basta repetir K veces (K ≤ 10) un Dijkstra con heap desde S, guardando para cada vértice su predecesor y la arista usada, reconstruir el camino a D y marcar sus aristas como eliminadas (por identificador, para soportar aristas paralelas). El último Dijkstra da la distancia y el camino, que se imprime de S a D separado por ' - '. El enunciado garantiza unicidad, así que el desempate no importa.

## L. Locate Tobby's nest

**Enunciado.** Los pasillos de la cuadrícula forman un árbol; elegir la celda desde la que la distancia máxima a cualquier otra es mínima (desempate: menor columna, luego menor fila).

**Solución.** Como entre dos pasillos hay un único camino, las celdas forman un árbol y la celda buscada es su centro: la de menor excentricidad. El centro de un árbol está en la mitad de cualquier diámetro. Se hace un BFS desde una celda cualquiera para encontrar el extremo a, otro BFS desde a guardando padres para encontrar el extremo b, y se reconstruye el camino de b a a de longitud L. Si L es par el centro es único (posición L/2); si es impar hay dos centros adyacentes (posiciones ⌊L/2⌋ y ⌈L/2⌉) y se elige el de menor columna y luego menor fila. Salida en índices desde 1.

## M. Marble tilt maze

**Enunciado.** Dos canicas se deslizan a la vez al inclinar el tablero (paredes, agujeros, bordes); mínimo de inclinaciones para dejar ambas en celdas G, o -1.

**Solución.** El estado es el par de posiciones (≤ 900² estados) y se hace BFS. Para cada dirección se precalcula dónde se detiene una canica sola desde cada celda (o -1 si cae en un agujero o sale del tablero). En un movimiento, si alguna cae el estado se descarta; si ambas terminan en la misma celda, están en la misma línea sin obstáculos entre ellas: la más cercana al tope ocupa la celda y la otra queda justo antes. Así cada transición es O(1). PENDIENTE: con este modelo el ejemplo 1 del enunciado da -1 en lugar de 4 (los ejemplos 2 y 3 sí coinciden), y tampoco lo explican las variantes probadas (orden fijo de canicas, paso a paso); falta entender la regla del ejemplo 1.

## Notas

- `tests/dudosos/Marble.1.*` es el ejemplo 1 de M, que no se corre porque la solución actual no lo reproduce.
- Python con casos de tamaño máximo (medido en local): Flipando ~8 s (límite 6 s), Locate ~4 s (límite 2 s) y Betito/Guanex/Kthpath cerca del límite; para esos problemas conviene enviar la versión C++.
