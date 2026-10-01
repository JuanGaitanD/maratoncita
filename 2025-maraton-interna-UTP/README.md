# Maratón Interna de Programación UTP 2025

- Fecha: 2025
- Juez: ninguno. Sin enunciados guardados; reconstruidos a partir del código.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| - | Borrar | `Borrar.py` / `Borrar.cpp` | Cadenas | O(|s|) | local-ok |
| - | Guanex (cola de prioridad) | `Guanex.py` / `Guanex.cpp` | Heap | O(n log n) | local-ok |
| - | K cuadrado | `Kcuadrado.py` / `Kcuadrado.cpp` | Aritmética modular | O(q) | local-ok |

## Borrar (`Borrar`)

**Enunciado:** Línea 1: un texto. Línea 2: un conjunto de caracteres prohibidos entre corchetes, p. ej. [aeiou]. Borrar del texto los prohibidos, no añadir un carácter si es igual al último que quedó en el resultado (así se comprimen las repeticiones) y recortar los espacios de los extremos. (enunciado reconstruido a partir del código del usuario)

**Solución:** Se recorre el texto una vez. Los caracteres prohibidos (lo que va entre los corchetes de la segunda línea) se guardan en un set para consultarlos en O(1). Cada carácter permitido se agrega solo si es distinto del último carácter del resultado; esto reproduce la variable temp del código original y hace que, al borrar una vocal entre dos espacios, no queden espacios dobles. Al final se quitan los espacios de los extremos (strip). Todo es lineal en la longitud del texto. En C++ también se quitan los \r finales para tolerar entradas con fin de línea de Windows.

## Guanex (cola de prioridad) (`Guanex`)

**Enunciado:** N operaciones: "1 x" inserta x, "2" elimina el mínimo (si existe), "3" imprime el mínimo actual o "Empty!" si no hay elementos. (enunciado reconstruido a partir del código del usuario)

**Solución:** La versión del usuario buscaba el mínimo con min() en una lista, lo que cuesta O(n) por operación y O(n²) en total, demasiado para N grande. Un min-heap resuelve todo: heappush para insertar, heappop para borrar el mínimo y h[0] para consultarlo, cada una en O(log n) o menos. En C++ se usa priority_queue con greater<> para que el tope sea el mínimo. Borrar con el heap vacío se ignora, igual que en el código original. La salida se acumula y se imprime de una vez para que la E/S sea rápida.

## K cuadrado (`Kcuadrado`)

**Enunciado:** Q consultas con un entero k cada una; imprimir k² mod (10^18 + 3). (enunciado reconstruido a partir del código del usuario)

**Solución:** La fórmula es directa: la respuesta es k² mod M con M = 10^18 + 3. El único detalle es el desborde: con k cerca de 10^18, k² tiene unos 120 bits y no cabe en 64. Python maneja enteros arbitrarios, así que basta k**2 % M. En C++ primero se reduce k módulo M y luego se multiplica en unsigned __int128, una extensión de GCC que admiten los jueces habituales, antes de tomar el módulo. Cada consulta cuesta O(1). Se lee todo de una vez y se escribe una línea por consulta con salida rápida.
