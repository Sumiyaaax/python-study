k = int(input())
a, b = map(int, input().split())
answer = 'NG'
for i in range(a, b + 1):
    if i % k == 0:
        answer = 'OK'
        break

print(answer)