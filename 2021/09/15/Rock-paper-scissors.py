x, y = map(int, input().split())
answer = x
if (x == 0 and y == 1) or (x == 1 and y == 0):
    answer = 2
elif  (x == 1 and y == 2) or (x == 2 and y == 1):
    answer = 0
elif  (x == 0 and y == 2) or (x == 2 and y == 0):
    answer = 1
print(answer)
