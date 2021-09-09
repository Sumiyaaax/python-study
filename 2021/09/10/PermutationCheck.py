N = int(input())
numList = list(map(int, input().split()))
numList.sort()
answer = "Yes"
for i, x in enumerate(numList):
    if x != i + 1:
        answer = "No"
        break
print(answer)