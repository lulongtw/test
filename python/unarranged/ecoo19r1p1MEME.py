#一開始有n件衣服 每天穿一件乾淨的 然後衣服就變髒了  
#如果當天沒有乾淨衣服了 就先洗所有的衣服 如果去參加活動 乾淨衣服會+1
#鑒於n件衣服 還有之後 d天的活動 在d天內要洗幾次衣服?
#input
#  n=衣服幾件  m=有幾個活動 d有幾天
#下一行有m個數字 代表有活動的那一天
# 洗幾次衣服


for dataset in range(2):
    x = input().split()
    for i in range(len(x)) :
        x[i] = int(x[i])

    e = input().split()
    for i in range(len(e)) :
        e[i] = int(e[i])-1

    e.sort() #沒sort

    t = x[0]   #一開始tshirt數
    d = x[2]   #天數

    totalt = t  #所有衣服數
    l = 0    #洗衣次數
    i = 0    #步進天數
    n = 0    #活動天數的index 
    while d - i > 0 : #當總天數-步進天數(一開始是第0天)到最後一天 也就是n-1天時 false跳出
        if t == 0 :   #每天一開始就檢查有沒有乾淨的衣服 如果乾淨衣服0就去洗
            l = l + 1
            t = totalt  #乾淨衣服=總衣服
        if n < len(e) and i == e[n] :  #如果遇到活動 n是自己另外步進
            n = n + 1   
            totalt = totalt + 1
            t = t + 1
        t = t - 1   #每天結束 乾淨衣服-1
        i = i + 1
    print(l)
