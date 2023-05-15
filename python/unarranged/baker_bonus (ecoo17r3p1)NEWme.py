# F代表加盟商
# D代表天數
# 下面D行 每一行都會有F個數字 代表每個加盟商當天營業額

# 檢查每一D行的總和跟每一F列的總和共有幾個13的倍數

x = input().split()
f = int(x[0])
d = int(x[1])

g = []
m = 0

for i in range(d) :
    y = input().split()
    for j in range(f) :
        y[j] = int(y[j])
    if sum(y) % 13 == 0 :
        m = m + sum(y) // 13
    g.append(y)
print(m)

s = []

for j in range(f) :
    for i in range(d) :
        s.append(g[i][j])
    if sum(s) % 13 == 0 :
        m = m + sum(s) // 13
    s = []

print(m)

