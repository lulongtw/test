n = int(input())

x = []
z = []
for i in range(n * 2) :
    for j in range(n) :
        z.append(".")
    x.append(z)
    z = []
        
d = input()
row = n
ps = ""

for i in range(len(d)) :   
    if d[i] == "+" :
        if ps == "up" :
            row = row - 1
        x[row][i] = "/"
        ps = "up"   
    elif d[i] == "-" :
        if ps == "down" :
            row = row + 1
        x[row][i] = "\\"
        ps = "down"   
    elif d[i] == "=" :
        if ps == "up" :
            row = row - 1
        x[row][i] = "_"
        ps = ""

for i in range(2 * n) :
    if x[i] != ["."] * n :
        print("".join(x[i]))





# ans = []

# for i in range(n * 2) :
#     if x[i] != ["." ]* n  :
#         ans.append(x[i])

# x = ""
# for i in range(len(ans)) :
#     for j in range(len(ans[i])) :
#         x = x + ans[i][j]
#     print(x)
#     x = ""
