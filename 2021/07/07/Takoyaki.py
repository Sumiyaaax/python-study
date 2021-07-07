n, x, y = map(int, input().split())
if n % x == 0:
    print((int(n / x)) * y)
else:
    print((int(n / x) + 1) * y)
