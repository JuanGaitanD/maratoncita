n = input()
m = n.count(n[0])	

if m == 2 or m == 3:
    n = n.replace(n[0], "")

    if n.count(n[0]) == (5 - m):
        print("YES")
    else:
        print("NO")
else:
    print("NO")