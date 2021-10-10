N = int(input())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
aMax = 0
bMin = 1000
for i in aList:
    if aMax < i:
        aMax = i

for i in bList:
    if bMin > i:
        bMin = i

if aMax >= bMin:
    print(0)
else:
    print(bMin - aMax + 1)