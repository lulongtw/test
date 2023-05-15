#ab兩隊的比賽 我們知道兩隊總分  還有每分在第幾秒的時候發生的


#問
#第1440秒時 上半場總分幾分?  
#有幾次比分"超前"的情形?

#input
# 第一行a 代表A隊得幾分
#下a行是a隊得分的時間 按大小排列
#接下來是b對目前的得分 
# 下b行是b隊得分的時間 按大小排列

a = 0
b = 0
lp = 0

ap =[]
for i in range(int(input())) :
    ap.append(int(input()))
bp =[]
for i in range(int(input())) :
    bp.append(int(input()))

all = ap + bp
all.sort()
k = 0

if all[0] in ap :
    lead = "a"
else :
    lead = "b"


for i in range(len(all)) :
    if all[i] in ap :
        a = a + 1
        if a > b and lead == "b":
            lead = "a"
            lp = lp + 1
    elif all[i] in bp :
        b = b + 1
        if b > a and lead == "a":
            lead = "b"
            lp = lp + 1
    if all[i] >= 1440 and k == 0:
        point = a + b
        k = 1



print(point-1)
print(lp)
