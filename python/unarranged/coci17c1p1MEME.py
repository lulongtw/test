# 檢21點
# 輸入n代表目前手上幾張牌
# 下n行代表手上的牌號碼們
# 檢查牌庫中會讓手上牌爆21點的牌 跟不會爆21點的牌誰是多誰少
# 輸出要不要再抽一張



deck = [0,0,4,4,4,4,4,4,4,4,4,12,4]

n = int(input())
h = 0
for i in range(n) :
    c = int(input())
    h = h + c
    deck[c] = deck[c] - 1
if sum(deck[21-h+1:]) > sum(deck[:21-h+1]) :
    print("no")
else :
    print("yes")


