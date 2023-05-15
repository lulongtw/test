def clean(x) :
    digit = []
    new = ""
    i = 0
    while x[i] != "@" :
        if x[i] != "." :
            new = new + x[i]
        i = i + 1   
    x = new + x[i:]
    for i in range(len(x)) :
        if x[i]  == "@" :
            s = i
        if x[i] == "+" :
            digit.append(i)
    if len(digit) > 0 and digit[0]< s :     
        x = x[:digit[0]] + x[s:]      
    x = x.lower()
    return x

    
n = int(input())
lst = []
for i in range(n) :
    lst.append(clean(input()))
ans = set()

for i in lst :
    if i not in ans :
        ans.add(i)
print(len(ans))



        
     
