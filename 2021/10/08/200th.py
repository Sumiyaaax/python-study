N, K = map(int, input().split())
for i in range(K):
    if N % 200 == 0:
        N = N // 200
    else:
        nStr = str(N) + "200"
        N = int(nStr)
print(N)