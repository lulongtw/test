#ab兩隊的比賽 我們知道兩隊總分  還有每分在第幾秒的時候發生的


#問
#第1440秒時 上半場總分幾分?  
#有幾次比分"超前"的情形?

#input
# 第一行a 代表A隊得幾分
#下a行是a隊得分的時間 按大小排列
#接下來是b對目前的得分 
# 下b行是b隊得分的時間 按大小排列

asc = 0
bsc = 0
tar =0
A = []
B = []

atotal = int(input())

for ai in range(atotal) :
    A.append((int(input())))
   
btotal = int(input())
for bi in range(btotal) :
    B.append((int(input())))

AB = A + B
AB.sort()
lead = ""  
#沒設lead 會有先前a隊領先 然後比分打平 a隊再取得領先
#tar會多算這種情形  規則是要從落後 然後超前 才能算tar

for i in AB : #不要亂用range
    if i in A :
        asc = asc + 1
        if asc > bsc and asc == bsc + 1 and lead == "B":
            tar = tar + 1
        if asc > bsc :   #這個if的位置很重要  剛剛打在上面那個if之前 會讓下面if無法進第3個and條件
            lead = "A"

    elif i in B :
        bsc = bsc + 1
        if bsc > asc and bsc == asc + 1 and lead == "A":
            tar = tar + 1
        if bsc > asc :         
            lead = "B"
            
ans = 0
kk = 0
while ans == 0 :  #天才
    if AB[kk] >= 1440 :
        ans = len(AB[:kk])
    kk = kk + 1

print(ans)
print(tar)