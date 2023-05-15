x = input().split()
n = int(x[0])
d = int(x[1])

trolley = input().split()
for i in range(n) :
    trolley[i] = int(trolley[i])

for i in range(d) :
    v = int(input())
    f = sum(trolley[:v])
    s = sum(trolley[v:])
    # last = max(f,s)
    if f >= s :
        trolley = trolley[v:]
        print(f)
    else :
        trolley = trolley[:v]
        print(s)
    