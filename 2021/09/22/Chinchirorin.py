a, b, c = map(int, input().split())
answer = 0
if a == b:
    answer = c
elif b == c:
    answer = a
elif c == a:
    answer = b
print(answer)