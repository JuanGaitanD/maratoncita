# Práctica Codeforces / LeetCode 2025

- Fecha: 2025
- Juez: ninguno. Ejercicios de práctica sin juez; enunciados reconstruidos. Referencia: https://leetcode.com/problems/maximum-subarray

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| - | Bubble sort | `BubbleSort.py` / `BubbleSort.cpp` | Ordenamiento | O(n²) | local-ok |
| - | Maximum subarray | `MaximumSubarray.py` / `MaximumSubarray.cpp` | Kadane / DP | O(n) | local-ok |

## Bubble sort (`BubbleSort`)

**Enunciado:** Leer n y n enteros; imprimirlos en orden ascendente con el algoritmo de burbuja. (El original ordenaba un arreglo fijo; se cambió para que lea la entrada.) (enunciado reconstruido a partir del código del usuario)

**Solución:** En cada pasada i se comparan pares de elementos vecinos y se intercambian si están desordenados. Así, el mayor de la parte que falta "sube" hasta la posición n − i − 1. Por eso el ciclo interno solo llega hasta n − i − 1: lo que está más a la derecha ya está en su lugar. Después de n − 1 pasadas el arreglo queda ordenado. Son O(n²) comparaciones, aceptable para n pequeño, aunque en competencia normalmente se usaría sort. Es el mismo código que el usuario tenía en bubbleSort.cpp y problemas.py, ahora leyendo de la entrada estándar.

## Maximum subarray (`MaximumSubarray`)

**Enunciado:** Leer n y n enteros; imprimir la mayor suma de un subarreglo contiguo no vacío (LeetCode 53). (enunciado reconstruido a partir del código del usuario)

**Solución:** El primer intento del usuario probaba todos los inicios y acumulaba sumas, O(n²). El algoritmo de Kadane, que el usuario dejó comentado, lo hace en O(n): cur es la mejor suma de un subarreglo que termina en la posición actual. Si cur era negativo conviene empezar de nuevo, así que cur = max(cur, 0) + x, y best guarda el mayor cur visto. Como best empieza en el primer elemento (o en −∞ en C++), funciona aunque todos los números sean negativos: la respuesta es entonces el mayor de ellos. Usa memoria constante.
