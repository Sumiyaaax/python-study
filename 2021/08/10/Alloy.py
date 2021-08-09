gold, silver = map(int, (input().split()))
answer = "Alloy"
if gold > 0 and silver == 0:
    answer = "Gold"
elif gold == 0 and silver > 0:
    answer = "Silver"
print(answer)