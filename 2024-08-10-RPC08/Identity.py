# Tela: 4x^2 sin(t) <= a, con t <= pi/4 (paraguas plano). Las puntas forman un octagono
# regular de radio R = x sin(t/2)/sin(pi/8); area seca = 2*sqrt(2)*R^2.
import math
a, x = map(float, input().split())
s = a / (4 * x * x)
t = math.pi / 4 if s >= math.sin(math.pi / 4) else math.asin(s)
R = x * math.sin(t / 2) / math.sin(math.pi / 8)
print("%.10f" % (2 * math.sqrt(2) * R * R))
