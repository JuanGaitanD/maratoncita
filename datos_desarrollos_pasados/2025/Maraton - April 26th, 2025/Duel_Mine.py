n = int(input())
total_cards = (n*2)
cards = [i for i in range(1, total_cards+1)]
f = []
puntajes = []

for i in range(n):
    p = int(input())
    cards.pop(cards.index(p))
    f.append(p)

for i in range(n-1):
    count = 0
    for j in range(n):
        if cards[j] > f[j]:
            count += 1
    
    puntajes.append(count)
    cards = cards[1:] + [cards[1]]

print(min(puntajes), max(puntajes))
