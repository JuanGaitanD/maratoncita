# Triangulos con 3 vertices del n-gono convexo: C(n, 3) mod 1e9+7 (Python maneja n hasta 1e18).
import sys
def main():
    d = sys.stdin.buffer.read().split()
    M = 1000000007
    print("\n".join(str(n * (n - 1) * (n - 2) // 6 % M) for n in map(int, d[1:1 + int(d[0])])))
main()
