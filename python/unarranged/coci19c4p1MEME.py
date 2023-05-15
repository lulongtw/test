n = int(input())


sumliquid = 0
glasses = []
for i in range(n) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    sumliquid = sumliquid + x[0]
    x[0] = 0
    glasses.append(x[1])
    
glass = glasses.copy()
maxidx = []
n0 = 0

while glasses != [0]*n :
    maxidx.append(glasses.index(max(glasses)))
    glasses[glasses.index(max(glasses))] = 0

for i in range(n) :
    if sumliquid >= glass[maxidx[i]] :
        glass[maxidx[i]] = glass[maxidx[i]]
        sumliquid = sumliquid - glass[maxidx[i]]
    else :
        glass[maxidx[i]] = sumliquid
        sumliquid = 0
       

for i in range(n) :
    if glass[i] == 0 :
        n0 = n0 + 1
    glass[i] = str(glass[i])
print(n0)
print(" ".join(glass))
