import math
N = int(input())
tax = 1.08
listPrice = 206
price = math.floor(N * tax)
if price < listPrice:
    print('Yay!')
elif price == listPrice:
    print('so-so')
else:
    print(':(')
