# Maratón — 26 de abril de 2025

- Fecha: 2025-04-26
- Juez: ninguno. Sin enunciado guardado; problema "Duel" reconstruido a partir de `Duel_AI.py` y `Duel_Mine.py`.

| Letra | Problema | Archivo | Tema | Complejidad | Estado |
|---|---|---|---|---|---|
| - | Duel | `Duel.py` / `Duel.cpp` | Greedy / dos punteros | O(n log n) | local-ok |

## Duel (`Duel`)

**Enunciado:** Hay cartas numeradas de 1 a 2n; Alice tiene n (dadas una por línea) y Bob el resto. En n rondas cada uno juega una carta y gana quien juegue la mayor. Imprimir la puntuación mínima y la máxima que puede obtener Alice. (enunciado reconstruido a partir del código del usuario)

**Solución:** Se ordenan las dos manos. Para calcular el máximo de victorias de una mano H1 contra H2 se usa un greedy: recorremos H1 de menor a mayor con un puntero w sobre la carta más pequeña de H2 que aún no se ha vencido; si la carta actual de H1 la supera, sumamos una victoria y avanzamos w. Si no la supera, esa carta se usa para perder contra una carta grande. Así, el máximo de Alice es wins(Alice, Bob). Su mínimo es n − wins(Bob, Alice), porque cada ronda la gana uno de los dos. El intento manual del usuario solo probaba rotaciones; esta es la idea de Duel_AI.py simplificada.
