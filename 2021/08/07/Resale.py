n = int(input())
valueList = list(map(int, input().split()))
costList = list(map(int, input().split()))
answer = 0
for i in range(n):
    if valueList[i] > costList[i]:
        answer += valueList[i] - costList[i]
print(answer)
