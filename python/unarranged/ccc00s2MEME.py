#有m個溪流 從左到右 編號為1~m
#往下流可能會分裂(l.fork r.fork)溪流數(m?)就會+1 或是合而為一就會 -1
#一旦分裂或匯流 都會重左到右重新編號 不會超過100個
#input
#第一行n 最初的河流數
#下n行從左至右給出每個stream的flow
#每個分裂都會有3行input
#一行有99 表明是split
#一行是數字 該分裂stream的號碼
#該flow 分裂成左邊的機率 
#有會留有兩個輸出
#一個是88 代表匯流
#一個是向右側溪流合併的號碼
#77end
#最後有幾條stream 每個stream有幾個flow

ini = int(input())
num = []

for i in range(ini) :
    num.append(int(input())) #每次都忘記可以直接append進[] 都會在上面開個s = int(input())

while True :
    x = int(input())
    if x == 77 :
        print(num)
        break
    elif x == 99 :
        spn = int(input()) -1 #幹真的很賤ㄟ  這個編號跟py的編號不一樣
        spp = int(input())
        left = []
        left.append(round(num[spn] * spp / 100))
        right = []
        right.append(round(num[spn] * (100-spp) / 100))
        new = num[:spn]   #到底要pop還remove  結果不用? 思考到到幾怎把r跟l加進去 用:切片把舊的分成兩半?
        newl = num[spn+1:]
        num = new + left + right + newl
    elif x == 88 :
        spj = int(input()) -1
        newj = []
        newj.append(num[spj] + num[spj+1])
        new = num[:spj]
        newl = num[spj+2:]
        num = new + newj + newl

