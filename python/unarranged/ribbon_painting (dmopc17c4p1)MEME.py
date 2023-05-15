x = input().split()
n = int(x[0])
q = int(x[1])


ribbon = []
for i in range(q) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    ribbon.append(x)

ribbon.sort()

print(ribbon)

maxr = 0
blue = 0

for i in ribbon :
    if i[0] <=  maxr :
        if i[1] > maxr :
            blue = blue + i[1] - maxr
            maxr = i[1]
    else :
        blue = blue + i[1] - i[0]
        maxr = i[1]
print(blue)
