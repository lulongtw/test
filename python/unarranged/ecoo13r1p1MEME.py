n = int(input())
t = 0
s = 0

while True :
    d = input().lower()
    if d == "eof" :
        break
    elif d == "take" :
        t = t + 1
    elif d == "serve" :
        s = s + 1
    elif d == "close" :
        n = n + t
        if n >= 1000:
            n = n - 999
        print(t,t-s,n)
        t = 0
        s = 0    