N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

z = 0
c = False
for d in D:
    if d[0] != d[1]:
        z = 0
    else:
        z += 1
        if z >= 3:
            c = True
            break

if c:
    print('Yes')
else:
    print('No')
