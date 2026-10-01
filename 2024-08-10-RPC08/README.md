# RPC 2024 - 8th Activity (Competitive Programming Network)

- Fecha: 2024-08-10
- Juez: https://redprogramacioncompetitiva.com/contests/2024/08
- Enunciados: `datos_desarrollos_pasados/2024/Training 10 Aug/ProblemsetRPC08.pdf`
- Probar: `python tools/test.py 2024-08-10-RPC08` (tests en `tests/`; fuerzas brutas y generador de casos grandes en `tests/brute/`)

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| A | Alphabetical Athletes | `Athletes.py` / `Athletes.cpp` | Cadenas / ordenamiento | O(|s| log |s|) | local-ok |
| B | Bright Beacons | `Beacons.py` / `Beacons.cpp` | BFS / visibilidad con pendientes | O(r*c*(r+c)) | local-ok |
| C | Cellar Chase | `Cellar.py` / `Cellar.cpp` | Parsing con pila / grafos serie-paralelo | O(|s|) | local-ok |
| D | Document Dimensions | `Document.py` / `Document.cpp` | Greedy + busqueda binaria / poda | O(sum_W h(W) log n) con poda | local-ok |
| E | Euroexpress | `Euroexpress.py` / `Euroexpress.cpp` | Ad hoc / geometria | O(n) | local-ok |
| F | Football Figurines | `Football.py` / `Football.cpp` | DP / conteo (Fibonacci) | O(n + q) | local-ok |
| G | Genius Gamer | `Gamer.py` / `Gamer.cpp` | DP con estados por color | O(13 * 4^4 * 2^4) | local-ok |
| H | Haggling over Hours | `Haggling.py` / `Haggling.cpp` | Flujo maximo / corte minimo de vertices | O(n^2) | local-ok |
| I | Inconspicuous Identity | `Identity.py` / `Identity.cpp` | Geometria / trigonometria | O(1) | local-ok |
| J | Jog in the Fog | `Jog.py` / `Jog.cpp` | Probabilidad / cota inferior | O(n) | local-ok |
| K | Keeping Keys | `Keys.py` / `Keys.cpp` | Greedy / cadenas | O(|s|) | local-ok |
| L | Longbottom Leap | `Longbottom.py` / `Longbottom.cpp` | Ad hoc / potencias de 2 | O(|s|) | local-ok |
| M | Montage Matrix | `Montage.py` / `Montage.cpp` | Conteo / ordenamiento | O(n log n) | local-ok |

## A. Alphabetical Athletes

**Enunciado.** Decidir si una palabra (ignorando mayusculas) tiene sus letras en orden alfabetico, directo o inverso.

**Solucion.** Se pasa la palabra a minusculas, porque solo la primera letra puede venir en mayuscula y no se distinguen. Luego basta comparar la palabra con su version ordenada ascendente y con su version ordenada descendente: si coincide con alguna, las letras aparecen en orden alfabetico (se permiten letras repetidas seguidas, como en Rommee). Ordenar 60 caracteres es instantaneo; tambien se podria revisar en un solo recorrido que todas las diferencias consecutivas tengan el mismo signo, pero la comparacion con sorted es mas corta y menos propensa a errores. Ejemplo: bekloppt ordenada da la misma cadena, Ente no coincide con ninguno de los dos ordenes.

## B. Bright Beacons

**Enunciado.** Cuadricula de alturas; una hoguera ve a otra en la misma fila o columna si ningun pico intermedio queda estrictamente por encima del segmento. Minimo de hogueras extra de la esquina NO a la SE.

**Solucion.** Es un camino minimo sin pesos: cada celda es un nodo y hay arista hacia las celdas visibles de su fila y su columna; la respuesta es la distancia BFS menos uno (la hoguera final ya existe). Para hallar las celdas visibles desde una celda se avanza en cada direccion guardando la pendiente maxima (altura relativa / distancia) de las celdas ya vistas. Una celda es visible si su pendiente es mayor o igual que esa maxima, porque entonces ningun pico intermedio queda por encima de la recta. Las pendientes se comparan con productos cruzados para evitar decimales. Cada celda revisa r+c celdas, a lo sumo 2 millones de pasos.

## C. Cellar Chase

**Enunciado.** Un sistema de corredores serie-paralelo descrito con (), (A+B) y (A*B). Los profesores entran por la entrada, solo avanzan hacia la salida y nunca deben dejar un camino libre entre la entrada y el troll. Cuantos se necesitan.

**Solucion.** Se define f(sistema). Un corredor simple necesita 1. En serie (A+B) todos barren A, se reunen en la union (que bloquea el paso) y luego barren B, asi que basta max(f(A), f(B)). En paralelo (A*B) los profesores no pueden regresar: quien entra a una rama nunca pasa a la otra, y mientras una rama este sucia alguien debe custodiar la entrada; por eso se necesita f(A)+f(B). Esto reproduce ambos ejemplos (2 y 5). La expresion se evalua con una pila de valores y operadores sin recursion, porque la cadena mide hasta un millon de caracteres y la anidacion puede ser muy profunda.

## D. Document Dimensions

**Enunciado.** Colocar n palabras en lineas (separadas por un espacio) eligiendo los saltos de linea para minimizar alto + ancho del papel.

**Solucion.** Para un ancho W fijo, el alto minimo lo da el greedy: meter en cada linea tantas palabras como quepan. Con prefijos q[j] = suma de (largo+1), la ultima palabra de una linea que empieza en i se encuentra con busqueda binaria (q[j] <= q[i]+W+1). Se prueban los anchos desde la palabra mas larga, pero primero se evalua W = raiz(S), cerca del optimo, para tener una buena cota. Luego se descarta cualquier W cuya cota inferior W + (S+1)/(W+1) no mejore, se corta la simulacion cuando el numero de lineas ya no puede mejorar y se termina cuando W+1 alcanza la mejor respuesta. Asi solo se simulan unos pocos anchos.

## E. Euroexpress

**Enunciado.** Una maleta p<=q<=r es valida si cada una de sus caras cabe en alguna de las n restricciones a x b. Maximizar el volumen.

**Solucion.** Ordenando las dimensiones de la maleta p<=q<=r, la cara mas grande es q x r, y las otras dos caras (p x q y p x r) son componente a componente menores o iguales que ella. Por tanto, si q x r cabe en alguna restriccion, todas las caras caben en esa misma. Dada una restriccion a<=b, lo mejor es q=a, r=b y p tan grande como permite p<=q, o sea p=a. El volumen es a*a*b y la respuesta es el maximo sobre todas las restricciones. Llega hasta 10^18 y cabe en long long. En el ejemplo 2, la restriccion 3x8 da 3*3*8 = 72.

## F. Football Figurines

**Enunciado.** Desde cada piso salen escaleras al piso +1 y al +2. Para cada consulta (s,t), sumar el numero de escaleras de todas las rutas distintas de s a t, modulo 1e9+7.

**Solucion.** La respuesta solo depende de k = t-s. Sea N(k) el numero de rutas que suben k pisos: N(0)=N(1)=1 y N(k)=N(k-1)+N(k-2), como Fibonacci, segun el primer paso. Sea E(k) la suma de escaleras de todas esas rutas. Si la ruta empieza con un paso de 1, aporta E(k-1) mas una escalera por cada una de sus N(k-1) rutas, y analogamente con el paso de 2. Entonces E(k) = E(k-1) + E(k-2) + N(k-1) + N(k-2) = E(k-1) + E(k-2) + N(k). Se precalcula hasta n en O(n) y cada consulta se responde en O(1). Ejemplo: E(4) = 7 + 3 + 5 = 15.

## G. Genius Gamer

**Enunciado.** Rummikub sin comodines: decidir si un conjunto de fichas (color, valor) se puede particionar en grupos (mismo valor, al menos 3 colores distintos) y escaleras (mismo color, al menos 3 valores consecutivos).

**Solucion.** Se recorren los valores de 1 a 13. El estado guarda, por cada color, el largo de la escalera abierta que llega al valor anterior: 0, 1, 2 o 3+ (256 estados). En cada valor, cada ficha presente va a su escalera (el largo sube, con tope 3) o al grupo de ese valor. Una escalera solo puede cerrarse si su largo es 0 o 3+, y eso pasa cuando el color no tiene ficha o la ficha se va al grupo. El grupo del valor debe tener 0, 3 o 4 fichas, porque solo cabe un grupo por valor. Si una escalera de 3+ termina y luego empieza otra, el caso equivale a extenderla. Al final todos los colores deben quedar en 0 o 3+.

## H. Haggling over Hours

**Enunciado.** Dados n intervalos, k es la cadena mas larga en la que cada inicio es al menos el fin anterior + 1. Quitar la minima cantidad de intervalos para que k baje.

**Solucion.** Primero se calcula con DP O(n^2) el largo L(i) de la mejor cadena que termina en i y R(i) el de la mejor que empieza en i. Solo importan los intervalos con L+R-1 = k, organizados en capas segun L. Hay que destruir todas las cadenas de largo k, que es un corte minimo de vertices entre la primera y la ultima capa, y por Menger es igual al flujo maximo con capacidad 1 por vertice. Para que haya O(n) aristas, cada capa se ordena por inicio y se encadena con nodos auxiliares: desde i se apunta al primer intervalo de la capa siguiente con inicio >= fin+1 y la cadena alcanza todo el sufijo. El flujo es a lo sumo n y se calcula con BFS de caminos aumentantes.

## I. Inconspicuous Identity

**Enunciado.** Un paraguas de 8 varillas de largo x; la tela entre varillas son triangulos isosceles y se dispone de a m^2 de tela. Maximizar el area protegida (proyeccion vertical).

**Solucion.** Si el angulo entre dos varillas vecinas es t, la tela usada es 8 * (1/2) x^2 sin t = 4x^2 sin t, que debe ser <= a. Las puntas forman un octagono regular de radio R con lado 2x sin(t/2) = 2R sin(pi/8). El area protegida es la del octagono, 2*sqrt(2)*R^2, que crece con t. El paraguas totalmente plano tiene t = pi/4 (R = x), asi que t = min(pi/4, asin(a/(4x^2))): si alcanza la tela se abre del todo, y si no se usa toda la tela disponible. En el ejemplo 1 sobra tela y la respuesta es 2*sqrt(2)*0.25 = 0.7071; en el ejemplo 2 el angulo es asin(0.1).

## J. Jog in the Fog

**Enunciado.** Jesse recorre en bucle una ruta de n celdas y empieza en una fase uniforme al azar. Sin ver nada, minimizar el tiempo esperado hasta encontrarlo (vale cruzarse a mitad de paso).

**Solucion.** Sea d la distancia Manhattan minima de tu posicion a una celda de la ruta: ninguna fase se puede encontrar antes del tiempo d. Despues, cada medio segundo se encuentra como mucho una fase nueva (una al cruzarse a mitad de paso y otra al llegar a la celda). Eso se logra exactamente si, al llegar, se corre por la ruta en sentido contrario a Jesse: se encuentran fases distintas en d, d+0.5, ..., d+(n-1)/2. Como la cota inferior se alcanza, la respuesta es el promedio d + (n-1)/4. Se calcula en enteros (4d+n-1)/4 y se imprime con dos decimales exactos. Ejemplos: 5 + 1/4 y 2 + 5/4.

## K. Keeping Keys

**Enunciado.** Se paga 1 centavo por tecla pulsada; mantener una tecla escribe repeticiones gratis y las mayusculas usan shift. Costo minimo de escribir el texto.

**Solucion.** Una tecla de letra mantenida sigue escribiendo aunque se pulse o se suelte shift, asi que cada bloque maximo de caracteres consecutivos con la misma tecla (sin importar mayusculas) cuesta 1, y la barra espaciadora igual. Shift se puede mantener mientras se escriben espacios, y solo una minuscula obliga a soltarlo. Por eso se suma 1 por cada bloque maximo de mayusculas, donde los espacios no rompen el bloque. Ejemplos: en Ll se pulsa shift, se mantiene l y se suelta shift, total 2. En A AaA las teclas son a, espacio, a (3) y hay dos bloques de shift (A A y la ultima A), total 5.

## L. Longbottom Leap

**Enunciado.** El hechizo con k palabras long cubre 32*2^(k-1) escalones consecutivos. Imprimir el hechizo mas corto que cubra toda la cadena (sin ceros al inicio ni al final).

**Solucion.** Como la cadena no tiene ceros al inicio ni al final, el primer y el ultimo escalon necesitan arreglo, y el hechizo, lanzado una sola vez desde el primer escalon, debe cubrir exactamente |s| escalones. La version mas corta (long) cubre 32 y cada long extra duplica la capacidad. Basta duplicar desde 32 hasta alcanzar |s| y contar las palabras. Con |s| <= 10^6 salen a lo sumo 16 palabras. Se imprime long repetido, separado por espacios. Ejemplos: una cadena de 32 caracteres sigue siendo long, y una de 33 necesita long long.

## M. Montage Matrix

**Enunciado.** Acomodar n personas en filas de a lo sumo w de forma que delante de cada uno solo haya personas estrictamente mas bajas.

**Solucion.** Cada columna de la foto es una secuencia estrictamente decreciente de atras hacia adelante, y como cada fila tiene a lo sumo w personas, hay a lo sumo w columnas. Dos personas de igual altura no pueden compartir columna, asi que si una altura aparece mas de w veces es imposible. Si ninguna aparece mas de w veces, se reparten las personas ordenadas por altura de forma ciclica en w columnas: las alturas iguales terminan en columnas distintas y cada columna queda estricta. Se ordena y se revisa si h[i] == h[i+w] para algun i (en Python, con Counter).
