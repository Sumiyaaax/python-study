r, d, x = map(int, input().split())
answerList = []

for i in range(10):
    if i == 0:
        answerList.append(r * x - d)
    else:
        answerList.append(r * answerList[i - 1] - d)

for a in answerList:
    print(a)
