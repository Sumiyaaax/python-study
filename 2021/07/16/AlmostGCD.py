n = int(input())
a = list(map(int, input().split()))

highestNum = 0
gcd = 0
for x in range(2, 1001):
    count = 0
    for y in a:
        if y % x == 0:
            count += 1
    if count >= highestNum:
        highestNum = count
        gcd = x
print(gcd)