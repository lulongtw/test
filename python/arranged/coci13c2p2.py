"""
題目：https://dmoj.ca/problem/coci13c2p2
給定一張座位圖，『o』代表有人，『.』代表沒人，
座位上每個人都會向相鄰座位(上下左右，左上左下，右上右下，共八個方向)的人握手，
如果座位都坐滿，直接計算所有握手次數(不可重複握手)，
如果還有座位，則讓mirko坐在可以讓握手次數最多的座位，
輸出總握手次數
"""

# 沒空位的解法
# 面對滿座的方法 讓[0,0]開始遍訪到[R,S] 每個座標遍訪所有座標 除了相減後絕對值大於等於二
# 以外 都是連成線(SHAKEHAND) 遍訪完該座標變"."沒人 繼續下一個

# # 有空位的解法
# # 有幾個空位就有幾種可能的答案
# # 把所有mirko的座位可以握手的數量都找一遍 然後抓出最大的

# 1.讀取
# 2.從第一個"o"開始遍訪到最後一個"o" 
# 3.檢查 如果出發與訪問的座標的 x and y座標 相減的絕對值都小於2 就可以算一個shake
# 4.把出發的座標換為"."
# 5.輸出


def start(r,s,seat) :  #找出圖中是"o"的點 
    for i in range(r) :
        for j in range(s) :
            if seat[i][j] == "o" :
                return[i,j]   


def search(r,s,x,y,se,shake) :  #遍訪每個是"o"的點 只要訪到的點跟xy距離小於2 就可以握手
    for i in range(r) :
        for j in range(s) :
            if se[i][j] == "o" and (abs(x-i) < 2 and abs(y-j) < 2) :
                shake = shake + 1
    return shake   

def count(r,s,se,shake) :  #遍訪圖中是"o"的點 作為出發點 然後用出發點遍訪所有"o"  
    for i in range(r) :      #決定出發點後 將出發點設為"." 這樣出發點才不會重複 握手也不會重複
        for j in range(s) :
            strt = start(r,s,se)
            if strt == None :
                break
            x = strt[0]
            y = strt[1]
            se[x][y] = "."
            shake = search(r,s,x,y,se,shake)
    return [shake]

def mirko(r,s,se) : #尋找"."作為mirko的座位
    mirko = []
    for i in range(r) :
        for j in range(s) :
            if se[i][j] == "." :
                mirko.append([i,j])
    return(mirko)

def recover(seat) :
    re = []
    for i in range(r) :
        for j in range(s) :
            if seat[i][j] == "o" :
                re.append([i,j])
    return re



#####################主程式開始##############
c = input().split()
r = int(c[0])
s = int(c[1])

seat = []
for i in range(r) :
    y = []
    x = ""
    x = input()
    for j in range(s) :        
        y.append(x[j])
    seat.append(y)

ans = []
shake = 0
mirkoseat = mirko(r,s,seat)


if len(mirkoseat) == 0 :
    print(count(r,s,seat,shake)[0]) 
else :
    re = recover(seat)
    for i in range(len(mirkoseat)) : 
        for j in range(len(re)) :
            seat[re[j][0]][re[j][1]] = "o"
        seat[mirkoseat[i][0]][mirkoseat[i][1]] = "o"      
        lst = count(r,s,seat,shake)
        ans.append(lst[0])
    print(max(ans))
        

            








