m = int(input())
d = int(input())

if m > 2 or (m == 2 and d > 18) :
    print("after")
elif m == 2 and d == 18 :
    print("special")
else :
    print("before")