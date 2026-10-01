import sys

def solve():
    n = int(sys.stdin.readline())
    alice_cards_list = []
    for _ in range(n):
        alice_cards_list.append(int(sys.stdin.readline()))

    # Ordenar las cartas de Alice
    alice_cards_list.sort()

    # Determinar y ordenar las cartas de Bob
    all_cards_set = set(range(1, 2 * n + 1))
    alice_cards_set = set(alice_cards_list)
    bob_cards_list = sorted(list(all_cards_set - alice_cards_set))

    # Función para calcular las victorias máximas de mano1 contra mano2
    def calculate_max_wins(hand1, hand2):
        wins = 0
        ptr1 = 0
        ptr2 = 0
        n_local = len(hand1) # Ambas manos tienen tamaño n

        while ptr1 < n_local and ptr2 < n_local:
            if hand1[ptr1] > hand2[ptr2]:
                # hand1[ptr1] puede vencer a hand2[ptr2]
                # Asegura esta victoria
                wins += 1
                ptr1 += 1 # Usar la carta de hand1
                ptr2 += 1 # Usar la carta de hand2
            else:
                # hand1[ptr1] no puede vencer a hand2[ptr2]
                # Necesitamos una carta más alta de hand1 para vencer a hand2[ptr2]
                # Avanza ptr1 para probar la siguiente carta de hand1
                ptr1 += 1
        return wins

    # Calcular puntuación máxima de Alice
    max_alice_score = calculate_max_wins(alice_cards_list, bob_cards_list)

    # Calcular puntuación máxima de Bob (jugando contra Alice)
    max_bob_score = calculate_max_wins(bob_cards_list, alice_cards_list)

    # Calcular puntuación mínima de Alice
    min_alice_score = n - max_bob_score

    # Imprimir resultados
    print(min_alice_score, max_alice_score)

# Ejecutar la solución
solve()