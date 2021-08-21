N, X = map(int, input().split())
priceList = list(map(int, input().split()))
total = 0
for i, price in enumerate(priceList):
    if i % 2 == 0:
        total += price
    else:
        total += price - 1
if total > X:
    print('No')
else:
    print('Yes')

