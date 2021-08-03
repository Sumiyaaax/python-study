a, b, t = map(int, input().split())
answer = 0
i = 1
while a * i <= t:
    answer += b
    i += 1
print(answer)