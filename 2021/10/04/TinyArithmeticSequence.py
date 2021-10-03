numList = list(map(int, input().split()))
numList.sort()
if numList[2] - numList[1] == numList[1] - numList[0]:
    print("Yes")
else:
    print("No")