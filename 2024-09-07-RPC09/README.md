# RPC 09 - 2024 (Competitive Programming Network, 9th Activity)

Fecha: 2024-09-07

Juez: https://redprogramacioncompetitiva.com/contests/2024/09

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Alien Attack | Alien.py / Alien.cpp | Grafos / simulación + DSU en reversa | O((n+m) log n) | local-ok |
| B | Broken Borders | Broken.py / Broken.cpp | Geometría + strings (arreglo de sufijos) | O((n + Σk) log n) | local-ok (py lento en el peor caso: usar C++) |
| C | Christmas Calories | Christmas.py / Christmas.cpp | Geometría / probabilidad | O(1) | local-ok |
| D | Discus Domination | Discus.py / Discus.cpp | Ventana deslizante | O(n) | local-ok |
| E | Elegant Exterior | Elegant.py / Elegant.cpp | Optimización / búsqueda ternaria | O(iteraciones) | local-ok |
| F | Fragmented Floor | Fragmented.py / Fragmented.cpp | Geometría ortogonal + emparejamiento bipartito | O(r·n + H·V·(H+V)) | local-ok |
| G | Gorgeous Garment | Gorgeous.py / Gorgeous.cpp | Búsqueda binaria + greedy | O(k log² n) | local-ok |
| H | Hungry Hunting | Hungry.py / Hungry.cpp | DP de cambio de monedas + divide y vencerás | O(n·w·log n) | local-ok |
| I | Icons in the Toolbar | Icons.py / Icons.cpp | Greedy / sumas alternadas | O(N) | local-ok |
| J | Jinxed Jewelry | Jinxed.py / Jinxed.cpp | Greedy / ordenamiento | O(n log n) | local-ok |
| K | K.O. Kids II | Kids.py / Kids.cpp | Probabilidad / DP | O(n·k) | local-ok |
| L | Legendary LAN-Party | Legendary.py / Legendary.cpp | Greedy / intercambio (regla de Smith) | O(n log n) | local-ok |
| M | Massive Mountains | Massive.py / Massive.cpp | Grafos / Dijkstra sobre pares + Floyd | O(n^4) | local-ok |

## A. Alien Attack

**Enunciado.** Cada día los trisolaranos destruyen la ciudad de mayor grado (desempate por menor índice, NY al final) y se pierden las ciudades que quedan desconectadas de NY. Se pide cuántos días faltan hasta que atacan NY.

**Solución.** La clave es que las ciudades perdidas forman componentes sin aristas hacia las sobrevivientes, así que nunca alteran los grados de éstas. Por eso el orden en que se atacan las sobrevivientes coincide con la simulación pura que ignora la ETO: un heap de máximos por (grado, -índice) con borrado perezoso, excluyendo a NY. Con ese orden fijo, el resto es conectividad decremental offline: se insertan las ciudades en orden inverso uniendo con DSU a los vecinos ya presentes (NY está desde el inicio). Una ciudad cuenta como un día si al insertarla queda en la componente de NY, es decir, si seguía conectada cuando la atacaron. La respuesta es ese conteo más uno.

## B. Broken Borders

**Enunciado.** Dado un polígono simple y m piezas de borde (polilíneas), decidir si rotando, trasladando y reflejando piezas (reutilizables) se cubre exactamente todo el borde, con vértices sobre vértices.

**Solución.** Como no hay tres vértices consecutivos colineales, una pieza colocada debe coincidir con una cadena de aristas consecutivas del polígono. Cada par de aristas consecutivas se codifica con el token (|e1|², e1·e2, e1×e2, |e2|²), invariante a rotación y traslación. El texto es el polígono duplicado (2n tokens) y se construye su arreglo de sufijos. Cada pieza, en sus 4 variantes (espejo x→-x y reversa), se busca con búsqueda binaria y da un rango de sufijos; cada rango se pinta con la mayor longitud usando un DSU de 'siguiente sin pintar'. Con diferencias se marcan las aristas cubiertas; las piezas de una sola arista cubren toda arista de igual longitud. YES si todo queda cubierto.

## C. Christmas Calories

**Enunciado.** En una pista circular de radio r se ve hasta distancia l en línea recta. Caro está en un punto uniforme de la pista: probabilidad de no verla.

**Solución.** Si el ángulo central entre los dos puntos es φ, la distancia en línea recta es la cuerda 2r·sin(φ/2). Se ve a Caro si esa cuerda es a lo sumo l, es decir si φ ≤ 2·asin(l/(2r)). Por simetría φ es uniforme en [0, π], así que la probabilidad de verla es 2·asin(l/2r)/π y la pedida es su complemento. Si l ≥ 2r se ve toda la pista y la respuesta es 0. Se imprime con 10 decimales en ambas versiones; la precisión doble basta incluso con r = 10^9 y l = 1.

## D. Discus Domination

**Enunciado.** Elegir i ≤ j ≤ i+m para maximizar a_j - a_i.

**Solución.** Para cada destino j el mejor punto de partida es el mínimo de a en la ventana [j-m, j], que incluye a j (lanzar al mismo cuadro da 0, así que la respuesta nunca es negativa). Ese mínimo de ventana deslizante se mantiene con una deque monótona de índices con valores crecientes: al entrar j se sacan por detrás los índices con valor mayor o igual, y por delante los que salen de la ventana. La respuesta es el máximo de a_j menos el valor del frente de la deque. Cada índice entra y sale una sola vez, por lo que el total es lineal.

## E. Elegant Exterior

**Enunciado.** Casa de Nicolás: rectángulo w×h con diagonales y techo triangular de altura h. Con madera total n, maximizar el área del frente.

**Solución.** La madera usada es 2w + 2h + 2·sqrt(w²+h²) + 2·sqrt((w/2)²+h²) y el área es wh + wh/2 = 1.5wh. Con t = h/w la madera es w·f(t) y el área 1.5·t·w². Conviene usar toda la madera, luego w = n/f(t) y el área es 1.5·t·n²/f(t)², que depende solo de t y es unimodal. Una búsqueda ternaria de 200 iteraciones en t ∈ [0, 10] da el óptimo con precisión de sobra. Como el área escala con n², también bastaría hallar la constante una vez, pero la ternaria es igual de corta.

## F. Fragmented Floor

**Enunciado.** Partir un polígono ortogonal simple (n ≤ 3000) en el mínimo número de rectángulos.

**Solución.** Resultado clásico: mínimo = r - L + 1, donde r es el número de vértices reflejos y L el máximo de cuerdas 'buenas' (segmentos axiales internos entre dos vértices reflejos) que no se cruzan ni se tocan. Las cuerdas horizontales y verticales forman un grafo bipartito de cruces y, por König, L = H + V - emparejamiento máximo. Las cuerdas se hallan lanzando desde cada vértice reflejo un rayo en la dirección opuesta a su arista horizontal (o vertical) y buscando la primera pared que toca; si el punto de impacto es otro vértice reflejo, hay cuerda. El emparejamiento se calcula con Kuhn (caminos aumentantes).

## G. Gorgeous Garment

**Enunciado.** Vueltas con t_i puntos no decrecientes; k colores en orden con s_i puntos de hilo; cada color usa un bloque de vueltas con anchos no decrecientes (los ceros forman un prefijo). Maximizar las vueltas tejidas.

**Solución.** Si se pueden tejer P vueltas también se pueden P-1: se quita la primera vuelta y todo se corre a vueltas más baratas. Así que se busca P binariamente. Para un P fijo se recorre desde el último color hacia atrás con el estado (vueltas que faltan R, ancho máximo permitido W = ancho del color siguiente). Que un color tome el mayor ancho posible (≤ W y que su hilo alcance) deja R más chico y W más grande, ambos mejores, así que el greedy es óptimo. Ese ancho máximo se halla con búsqueda binaria sobre sumas prefijas. Es factible si R llega a 0.

## H. Hungry Hunting

**Enunciado.** Mínimo número de porciones para sumar exactamente w cuando el plato i siempre se sirve doble (vale 2c_i), para cada i.

**Solución.** Es el problema de mínimo de monedas ilimitadas con el conjunto {c_j : j ≠ i} ∪ {2c_i}. Rehacer la DP para cada i cuesta n²w, demasiado. Se usa divide y vencerás sobre los platos: solve(l, r, dp) recibe la DP con todos los platos fuera de [l, r]; para la mitad izquierda se agregan los platos de la derecha y viceversa. En la hoja solo falta agregar 2c_i y leer dp[w]. Cada plato se agrega O(log n) veces. Agregar la moneda v es dp[x] = min(dp[x], dp[x-v]+1).

## I. Icons in the Toolbar

**Enunciado.** 2N íconos cuadrados ordenados; ubicarlos en 2 filas × N columnas minimizando (alto total)·(ancho total).

**Solución.** La fila 1 contiene al mayor, s_1, y su alto es s_1. Si la fila 2 tiene alto s_j, los íconos s_1..s_{j-1} van en la fila 1, cada uno en su propia columna, y lo mejor es emparejarlos con s_j..s_{2j-2}, que no suman ancho. Los restantes s_{2j-1}..s_{2N} se emparejan de a dos consecutivos y aportan s_{2j-1} + s_{2j+1} + ... al ancho. Se prueba cada j entre 2 y N+1 con una suma prefija y una suma alternada desde el final, y se toma el mínimo de (s_1+s_j)·ancho(j). Todo cabe en long long.

## J. Jinxed Jewelry

**Enunciado.** n cadenas de a_i eslabones; abrir y cerrar un eslabón cuesta 1 minuto. Mínimo tiempo para formar un solo collar circular.

**Solución.** Cada eslabón abierto sirve para unir dos extremos. Si se abren x eslabones tomándolos de los extremos de las cadenas, quedan q piezas, y para cerrarlas en círculo hacen falta q uniones, así que se necesita x ≥ q. Para reducir q conviene consumir por completo las cadenas más cortas. Si se consumen las j más cortas (P_j eslabones) quedan n-j piezas y el costo es max(P_j, n-j); los eslabones que falten se sacan del extremo de otra cadena sin crear piezas nuevas. Se ordena y se toma el mínimo para 0 ≤ j < n.

## K. K.O. Kids II

**Enunciado.** n niños hacen en fila k obstáculos; un obstáculo superado una vez lo superan todos los siguientes. Glen elige su posición: maximizar la probabilidad de ser el primero en terminar.

**Solución.** Estado: dist[j] = probabilidad de que nadie haya ganado aún y el progreso global sea j obstáculos. Un niño parte de j, supera gratis esos y luego cada obstáculo i con probabilidad a_i. Se recorre con un acumulador acc(i) = acc(i-1)·a_i + dist[i]: el niño termina con probabilidad acc(k) y el nuevo progreso queda en i con probabilidad acc(i)·(1-a_{i+1}). Para la posición p, la probabilidad de que Glen gane es acc(k) calculado sobre la distribución tras p-1 niños, así que basta simular los n niños y tomar el máximo. Son n·k = 10^7 operaciones.

## L. Legendary LAN-Party

**Enunciado.** Ordenar n switches (costo por cm c_i, largo m_i) en una línea; el switch que empieza en la posición x paga c·x. Minimizar el costo total.

**Solución.** El switch k-ésimo paga c_k·(1 + suma de m de los anteriores). Por el argumento de intercambio entre vecinos, i debe ir antes que j cuando m_i·c_j < m_j·c_i, es decir, se ordena por m/c ascendente (regla de Smith de scheduling con pesos). La comparación se hace con productos enteros para evitar errores de punto flotante. Después se recorre el orden acumulando la posición y sumando c·posición. Los valores llegan a unos 2·10^17, que caben en long long.

## M. Massive Mountains

**Enunciado.** Dos personas parten de la estación 1 y ambas deben llegar a n. Hay dos compañías y nunca pueden usar a la vez teleféricos de la misma compañía. Tiempo mínimo.

**Solución.** Entre dos instantes en que ambos están quietos, si uno viaja con la compañía X el otro solo puede usar Y, y así sigue hasta que ambos queden quietos a la vez. Entonces cada fase es: A recorre un camino solo de X y B uno solo de Y (o al revés), y la fase dura el máximo de los dos. Con Floyd se calculan DX y DY (distancia 0 a sí mismo). Luego se corre un Dijkstra denso sobre pares (u, v) con transición (u,v)→(u',v') de costo min(max(DX[u][u'], DY[v][v']), max(DY[u][u'], DX[v][v'])). Son 5625 estados con 5625 transiciones cada uno.
