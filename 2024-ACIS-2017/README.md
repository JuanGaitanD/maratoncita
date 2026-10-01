# Maratón ACIS 2017 (práctica 2024)

- Fecha: 2017 (resuelto en 2024)
- Juez: ninguno. Enunciados originales: https://acis.org.co/archivos/Maraton/Problemas2017.pdf (el enlace ya no responde: "Page Not Found"), por eso los enunciados están reconstruidos.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| - | ACM (caminata del equipo) | `Acm.py` / `Acm.cpp` | Agrupación / sumas | O(S log S) | local-ok |
| - | Balance | `Balance.py` / `Balance.cpp` | Fuerza bruta | O(C³) | local-ok |

## ACM (caminata del equipo) (`Acm`)

**Enunciado:** Varios casos hasta EOF. Cada caso: N S; S líneas "a b d" (tramo de longitud d que sale del punto a); una línea con las velocidades de caminata de los integrantes. El equipo camina a la velocidad del más lento. Imprimir el menor tiempo entero (redondeado hacia arriba) de recorrer todos los tramos que salen de un mismo punto. (enunciado reconstruido a partir del código del usuario)

**Solución:** Siguiendo el código del usuario, los tramos se agrupan por su punto de partida y se suma la longitud total de cada grupo. Como el equipo debe ir junto, su velocidad es la mínima de la lista. Para cada grupo el tiempo es la suma dividida entre esa velocidad, redondeado hacia arriba; se calcula en enteros como (t + v − 1) / v para evitar errores de punto flotante. La respuesta es el mínimo entre todos los grupos. El original arrancaba el mínimo en 200 (podía quedarse corto) y tenía un while True sin manejo de EOF; ambas cosas se corrigieron.

## Balance (`Balance`)

**Enunciado:** Un objeto de peso W está en un platillo. Hay tres tipos de pesas (t1, t2, t3), con hasta C copias de cada una. Contar cuántas combinaciones (i, j, k) de copias equilibran la balanza, si todas las pesas van al platillo contrario o si un solo tipo acompaña al objeto. Entrada: C W, luego t1 t2 t3. (enunciado reconstruido a partir del código del usuario)

**Solución:** Se conservan las cuatro condiciones del código original. Si a = i·t1, b = j·t2 y d = k·t3, la balanza queda equilibrada cuando a + b + d = W (todas las pesas en el otro platillo) o cuando un tipo va con el objeto: W + a = b + d, W + b = a + d o W + d = a + b. Se recorren todas las ternas con tres ciclos anidados y se cuenta cada terna una sola vez aunque cumpla varias condiciones. Con C pequeño (unas decenas) la fuerza bruta O(C³) es suficiente. Si C fuera grande, se podría fijar (i, j) y despejar k en O(1).
