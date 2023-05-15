# 三個學生各有不同答題方法
# input題目數跟答案
# 輸出誰最多的那(些)人
# 應該有更文雅的方法



n = int(input())

a = "ABC" * n
b = "BABC" * n
g = "CCAABB" * n
ap = 0
bp = 0
gp = 0

ans = input()
for i in range(n) :
    if ans[i] == a[i] :
        ap = ap + 1
    if ans[i] == b[i] :
        bp = bp + 1
    if ans[i] == g[i] :
        gp = gp + 1

all = []
all.append(ap)
all.append(bp)
all.append(gp)

all.sort()
p = ""

if ap == max(all) :
    p = p + "a"
if bp == max(all) :
    p = p + "b"
if gp == max(all) :
    p = p + "g"
print(p)

