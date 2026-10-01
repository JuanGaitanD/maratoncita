from fractions import Fraction as fr
a = 10
b = 5

case = 326

f = fr(str(case))

entero = f.numerator // f.denominator
rem = f.numerator % f.denominator

print(f"{entero} {rem}/{f.denominator}")

c = a // b
d = a % b

print(f"{c} {d}/{b}")