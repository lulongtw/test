def distinct(x) :
    x = str(x)
    for i in x :
        if x.count(i) > 1 :
            return False
    return True

y = int(input())
ans = False
while not ans :
    y = y + 1
    ans = distinct(y)
print(y)
        










