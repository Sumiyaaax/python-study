P = int(input())
def getFactorial(i):
    tmp = 1
    for j in range(1, i + 1):
        tmp *= j
    return tmp

factorialList = list()
for i in range(1, 11):
    factorialList.append(getFactorial(i))
total = 0
answer = 0
for i in reversed(range(1, 11)):
    while factorialList[i - 1] <= P - total:
        total += factorialList[i - 1]
        answer += 1

print(answer)

