n, a, x, y = map(int, input().split())
answer = 0
if n < a:
    answer = n * x
else:
    answer = (a * x) + (n - a) * y
print(answer)