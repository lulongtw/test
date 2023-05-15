#貓會玩每個紙箱 會玩t天 就不玩了
#貓不完後 MANDY可以用了
#一旦有新盒子 貓也會等T天才會動它
#   在N天理 算有幾天因為貓而耽擱

x = input().split()
t = int(x[0])
n = int(x[1])
hb = []

for i in range(n) :
    hb.append(input())
bday = 0
i = 0
while n - i > 0 : #n - i想好久
    if hb[i] == "B" :        
        bday = bday + t  #box耀清掉 #不應該有box變數 這樣box有兩個的時候會變超多
    i = i + 1
    bday = bday - 1
    if bday < 0 :
        bday = 0
print(bday)      