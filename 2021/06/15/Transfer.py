a, b, c = map(int, (input().split()))
answer = c - (a - b) if c - (a - b) >= 0 else 0
print(answer)