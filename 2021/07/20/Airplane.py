p, q, r = map(int, input().split())
answer = p + q + r - max(p, q, r)
print(answer)