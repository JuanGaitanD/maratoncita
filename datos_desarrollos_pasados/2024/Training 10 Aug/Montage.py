n, w = map(int, input().split())
heights = list(map(int, input().split()))
message = ""

heights.sort(reverse=True)

for i in range(n-w):
    if(heights[i] <= heights[i+w] ):
        message = "no"
        break
else:
    message = "yes"

print(message)