days = int(input())
volumen_alcohol, volumen_others = map(int, input().split())
evapo_a, evapo_o = map(int, input().split())

volumen_alcohol = volumen_alcohol - (evapo_a * days)
volumen_others = volumen_others - (evapo_o * days)

if volumen_alcohol < 0:
    volumen_alcohol = 0
if volumen_others < 0:
    volumen_others = 0

print( volumen_alcohol * 100 / (volumen_alcohol + volumen_others) )