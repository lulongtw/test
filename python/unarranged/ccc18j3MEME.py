dis = []
x = input().split()
for i in range(len(x)) :
    dis.append(int(x[i]))


for i in range(5) :
    ans = ["","","","",""]
    ans[i] = 0
    while "" in ans :
        for j in range(i,4) :
            ans[j+1] = ans[j] + dis[j]
        for k in range(i-1,-1,-1) :
            ans[k] = ans[k+1] + dis[k]
    for i in range(len(ans)) :
        ans[i] = str(ans[i])        
    print(" ".join(ans))
 










