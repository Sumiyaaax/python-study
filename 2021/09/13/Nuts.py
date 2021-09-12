N = int(input())
numList = list(map(int, input().split()))
total = 0
for i in range(N):
    if numList[i] > 10:
        total += numList[i] - 10
print(total)
