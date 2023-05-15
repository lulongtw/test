n = int(input())

x = []
for i in range(n) :
    y = input().split()
    for j in range(len(y)) :
        y[j] = int(y[j])
    y.remove(y[0])
    x.append(y)


def issorted(lst) :
    if len(lst) == 1 :
        return True
    else :    
        for i in range(len(lst)-1) :
            if lst[i+1] < lst[i] :
                return False
    return True

for i in range(len(x)) :
    if issorted(x[i]) :
        single = True
    else :
        single = False
        break



def cut(lst) :
    for i in range(len(lst)) :
        if len(lst) > 2 :
            lst.pop(1)

for i in range(len(x)) :
    cut(x[i])

x.sort()

def last(lst) :
    for i in range(len(lst)-1):
        if lst[i+1][0] < lst[i][-1] :
            return False
    return True

if last(x) and issorted(x) :
    print("yes")
else :
    print("false")
            

