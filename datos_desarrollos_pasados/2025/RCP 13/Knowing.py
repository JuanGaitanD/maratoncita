h, m = map(int, input().split())

if h == ((h//30)*30) + (m/12):
    print('yes')
else:
    print('no')