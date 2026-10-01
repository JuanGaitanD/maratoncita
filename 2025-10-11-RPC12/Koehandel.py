# Si n > c apostar c+1 (ganas vaca); si n == c empatar con c; si n < c perder igual: apostar 0.
c, n = map(int, input().split())
print(c + 1 if n > c else (c if n == c else 0))
