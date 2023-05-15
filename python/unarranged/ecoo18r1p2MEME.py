#輸入
#n = 下面有幾行輸入
#每行輸入  第一個代表號碼 第二個代表這排有幾個需要判別的東西r 下面r個東西代表要判別的東西
# 針對每行出現的數字  抓出所有需要判別的數字裡最小的
# 輸出  數字 {出現最小號碼所在的行數}  

n = int(input())
lane = []

for i in range(n) :   
    row = list(input().split())
    lane.append(row)

for i in range(n) :
    for ii in range(len(lane[i])):
        lane[i][ii] = int(lane[i][ii])

x = []
s = 1000000000000
for row in range(n) :
    i = 2
    while i < len(lane[row]) : #加range幹嘛
        if s >= lane[row][i] : #北七min一個整數幹嘛
            s = lane[row][i]   #不能在這邊append因為這樣不是直接抓出所有最小的而是慢慢比較    
        i = i + 1

for row in range(n) :
    if s in lane[row][2:] :
        row = str(row+1)
        x.append(row)

z = "{" + ",".join(x) + "}"

print(f"{s}{z}")
        