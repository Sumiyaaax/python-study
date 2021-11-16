x = input()
if '.' in x:
    num = x[:x.find('.')]
else:
    num = x
print(num)