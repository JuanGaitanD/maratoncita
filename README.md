# Maratón de Programación

Ejercicios de maratón de programación (clases, entrenamientos RPC y competencias), resueltos en **Python 3 y C++11** con una explicación breve de cada uno. El repositorio se organiza por evento, cada uno en su propia carpeta.

## Material de impresión

[`Ejercicios-maraton.pdf`](Ejercicios-maraton.pdf): portada con índice (número, letra, problema, evento, tema, complejidad y página) y luego, por problema, enunciado resumido, explicación de ~100 palabras y el código en ambos lenguajes. Se regenera con `python tools/build_pdf.py`.

## Estructura de cada carpeta

- `Nombre.py` y `Nombre.cpp`: soluciones, con el nombre de archivo exacto que exige el juez.
- `tests/Nombre.N.in` / `.out`: ejemplos del enunciado más casos extra; `tests/brute/`: fuerzas brutas y generadores usados para validar.
- `README.md`: tabla resumen y explicación de cada problema.
- `problems.json`: metadatos (tema, complejidad, explicación, estado) de donde se genera el PDF.

El estado `local-ok` significa que Python y C++ pasan todos los casos locales; donde Python es lento se indica "usar C++ en el juez".

## Eventos

| Carpeta | Evento | Problemas | Juez |
|---|---|---|---|
| [`2024-05-04-RPC04/`](2024-05-04-RPC04/) | RPC 2024 - 4th Activity (Competitive Programming Network) | 10 | — |
| [`2024-08-10-RPC08/`](2024-08-10-RPC08/) | RPC 2024 - 8th Activity (Competitive Programming Network) | 13 | — |
| [`2024-09-07-RPC09/`](2024-09-07-RPC09/) | RPC 09 - 2024 (Competitive Programming Network, 9th Activity) | 13 | — |
| [`2024-ACIS-2017/`](2024-ACIS-2017/) | Maratón ACIS 2017 (práctica 2024) | 2 | — |
| [`2024-ejercicios-propios/`](2024-ejercicios-propios/) | Ejercicios propios 2024 | 8 | — |
| [`2025-04-26-maraton/`](2025-04-26-maraton/) | Maratón — 26 de abril de 2025 | 1 | — |
| [`2025-09-27-RPC11/`](2025-09-27-RPC11/) | RPC 11 de 2025 (Competitive Programming Network, 11th Activity) | 13 | — |
| [`2025-10-11-RPC12/`](2025-10-11-RPC12/) | RPC 12 - 2025 (Competitive Programming Network, 12th Activity) | 13 | — |
| [`2025-11-01-RPC13/`](2025-11-01-RPC13/) | RPC 13 de 2025: Competitive Programming Network, 13th Activity | 13 | — |
| [`2025-maraton-interna-UTP/`](2025-maraton-interna-UTP/) | Maratón Interna de Programación UTP 2025 | 3 | — |
| [`2025-practica-codeforces/`](2025-practica-codeforces/) | Práctica Codeforces / LeetCode 2025 | 2 | — |
| [`2026-04-11-RPC03/`](2026-04-11-RPC03/) | RPC 03 - 2026 (Competitive Programming Network, 3rd Activity) | 12 | — |
| [`RCP09-UTP/`](RCP09-UTP/) | UTP Open 2026 (RPC 09 de 2026) | 13 | — |
| [`2026-09-14-practica-clase/`](2026-09-14-practica-clase/) | Práctica de clase (UAM) | 5 | — |

La carpeta [`datos_desarrollos_pasados/`](datos_desarrollos_pasados/) conserva los enunciados (PDF) y los intentos originales tal como quedaron en cada maratón.

## Ejecución y pruebas

```bash
python 2026-04-11-RPC03/Pizza.py < 2026-04-11-RPC03/tests/Pizza.1.in
python tools/test.py 2026-04-11-RPC03          # corre py y cpp contra tests/ (C++ vía docker gcc:13)
python tools/test.py 2026-04-11-RPC03 Pizza    # un solo problema
```

## Licencia

MIT. Ver [LICENSE](LICENSE).
