這城市一次追蹤太多東西
先用迴圈desk抓出目標 檢查迴圈的下個元素是否相同
如果有就加一沒有就調出字典  再放進lst中供以後檢查
我也不知道這樣為什麼沒有通過 邏輯是通的但有夠複雜

解答版用迴圈分數做為目標 檢查desk內是否有連續
有連續就加一沒有就歸零 返回最大值
然後題目說要用最小的  主程式用分數range(1~6)完美的解決這個問題
因為range從最小開始 然後到最大  如果max有超過 否則都是記錄最小的


x = int(input())

desk = []
for i in range(x) :
    n = input().split()
    n[0] = int(n[0])
    n[1] = int(n[1])
    desk.append(n)

dic = {}
next = []
high = 1
old = []

if len(desk) == 1 :
    x = min(desk[0][0],desk[0][1])
    print(" ".join([str(x),str(1)]))
else :
    for i in range(len(desk)-1) :
        next.append(desk[i+1][0])
        next.append(desk[i+1][1])
        for j in range(2) :
            if desk[i][j] not in dic :
                dic[desk[i][j]] = 1
                if desk[i][j] in next :
                    dic[desk[i][j]] += 1
                    if dic[desk[i][j]] > high :
                        high = dic[desk[i][j]]
                else :                                
                    old.append([desk[i][j],dic[desk[i][j]]])
                    dic.pop(desk[i][j])
            else :
                if desk[i][j] in next :
                    dic[desk[i][j]] += 1
                    if dic[desk[i][j]] > high :
                        high = dic[desk[i][j]]
                else :                                
                    old.append([desk[i][j],dic[desk[i][j]]])
                    dic.pop(desk[i][j])
                
        next = []

    for i in dic :
        if dic[i] >= high :
            high = dic[i]
            old.append([i,dic[i]])

    big = 0
    ans = set()
    for i in range(len(old)) :
        if old[i][1] == high :
            ans.add(old[i][0])

    print(" ".join([str(high),str(min(ans))]))

