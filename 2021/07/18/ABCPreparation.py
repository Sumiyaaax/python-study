a = list(map(int, input().split()))
min = 100
for i in a:
    if i < min:
        min = i
print(min)