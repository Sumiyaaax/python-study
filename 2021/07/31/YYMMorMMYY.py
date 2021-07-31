s = input()

MM = [str(m).zfill(2) for m in range(1, 13)]
a = s[:2] in MM
b = s[2:] in MM

if a and b:
    print("AMBIGUOUS")
elif a and not b:
    print("MMYY")
elif not a and b:
    print("YYMM")
else:
    print("NA")