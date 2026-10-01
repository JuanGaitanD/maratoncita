# Se agrupan columnas no vacias consecutivas: 4 columnas = 'v', 8 = 'w'.
import sys
def main():
    t = sys.stdin.read().split()
    n, a, b = int(t[0]), t[1], t[2]
    res, run = [], 0
    for i in range(n + 1):
        if i < n and (a[i] != '.' or b[i] != '.'):
            run += 1
        elif run:
            res.append('v' if run == 4 else 'w'); run = 0
    print(''.join(res))
main()
