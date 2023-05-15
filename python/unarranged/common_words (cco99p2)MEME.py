x = input().split()
m = int(x[0])
k = int(x[1])


dic = {}
for i in range(m) :
    x = input()
    if x not in dic :
        dic[x] = 1
    else :
        dic[x] = dic[x] + 1

values = list(dic.values())
values.sort(reverse = True)
keys = list(dic.keys())

def ming(x) :
    num = [1]
    m = 1
    current = x[0]
    for i in range(1,len(x)) :
        if x[i] == current :
            num.append(m)
        else :
            m = i + 1
            num.append(m)
            current = x[i]
    return num


num = ming(values)
newdic = {}

for j in range(len(keys)) :
    valu = dic[keys[j]]
    if valu not in newdic :
        newdic[valu] = [keys[j]]
    else : 
        newdic[valu] = newdic[valu] + [(keys[j])]


if k in num :
    print(newdic[values[num.index(k)]])
else:
    print("")


