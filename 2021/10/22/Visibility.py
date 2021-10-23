H, W, X, Y = map(int, input().split())
sList = []
for i in range(H):
    sList.append(input())

X = X - 1
Y = Y - 1
for i in sList:
    print(i)

