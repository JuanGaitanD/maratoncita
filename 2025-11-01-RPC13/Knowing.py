# Con t minutos desde las 12: hora = t/2 grados y minuto = 6t mod 360. Asi t = 2h y basta 12h mod 360 == m.
h, m = map(int, input().split())
print("yes" if 12 * h % 360 == m else "no")
