a, b, c, k = map(int, input().split())
answer = 0
if a >= k:
    print(k)
else:
    if b >= k - a:
        print(a)
    else:
        print(a - (k - a - b))
