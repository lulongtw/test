input_file = open("tttt.in","r")
output_file = open("tttt.out","w")
lst = []
a = []
x = input_file.readline().rstrip()

while x != "" :
    for i in range(len(x)) :
        a.append(x[i])
    lst.append(a)
    a = []
    x = input_file.readline().rstrip()

sigle = 0
muliple = 0
def count(k,si,mul) :
    t = []
    for i in k :
        if i not in t :
            t.append(i)
    if len(t) == 1 :
        si = si + 1
    elif len(t) == 2 :
        mul = mul + 1
    return [si,mul]

ans = []
col = []
notstrait = []
s = []
for i in range(len(lst)) :
    ans = ans + count(lst[i],sigle,muliple)
    for j in range(len(lst)) :
        s.append(lst[j][i])
    col.append(s)
    ans = ans + count(col[i],sigle,muliple)
    s = []

x = []
for i in range(len(lst)-1,-1,-1) :
    s.append(lst[len(lst)-1-i][i])
    x.append(lst[i][i])
notstrait.append(s)
notstrait.append(x)

ans = ans + count(notstrait,sigle,muliple)
ans = ans + count(col,sigle,muliple)

a = 0
b = 0
i = 0
while i != len(ans) :
    if i % 2 == 0 :
        a = a + ans[i]
    else :
        b = b + ans[i]
    i = i + 1
print([a,b])
output_file.write(f"{a}\n")
output_file.write(f"{b}")

