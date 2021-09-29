N = int(input())
names = []
heightList = []
for i in range(N):
    S, T = map(str, input().split())
    names.append(S)
    heightList.append(int(T))
sorted_heightList = sorted(heightList, reverse=True)
for i in range(N):
    if sorted_heightList[1] == heightList[i]:
        print(names[i])
        break
