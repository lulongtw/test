n = int(input())

x = input().split()

for i in range(n) :
    x[i] = int(x[i])

high = max(x)
low = min(x)

hg_idx = x.index(high)
lw_idx = x.index(low)
z = []
if hg_idx <= lw_idx :
    print("no")

else :
    for i in range(lw_idx,hg_idx) :
        if x[i] > x[i + 1] :
            z.append("no")

if "no" in z :
    print("no")
else:
    print("ok")








# y = x[:]
# y.append(0)    


# y = y[lw_idx:hg_idx+1]

# g = y.sort()

# print(g)



# if y != y.sort() :
#     print("no")
# else :
#     print(high - low)
