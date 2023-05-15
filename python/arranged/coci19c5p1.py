"""
題目網址：https://dmoj.ca/problem/coci19c5p1
給聽一張圖，檢查圖內共有幾個矩形，就算圖形只有一個點，只要和其他圖形不相鄰，就算一個矩形

用遍訪的方式，從圖形左上遍歷到右下，每次遇到第一個『*』，就算一個矩形，接者開始
往右尋找直到不是『*』為止，然後再往下找直到不是『*』為止，接著把剛剛遍歷的座標全變為『.』
然後回到回圈開頭繼續找下去直到結束

這題其實對圖形的定義沒有很清楚，並沒有定義題目只會出現矩形，
所以那時在想題目時因為這個困擾蠻久，
看到下方有討論時才知道，題目只會出現矩形
"""

x = input().split()
a = int(x[0])
b = int(x[1])

xx = []
g = []
for i in range(a) :        
    x = input() + "."       #在每個row最右邊都加個「.」防止遍歷時超出index
    for j in range(b+1) :   #把圖上每個點都變成list方便之後變動，b+1是因為已經加『.』了
        g.append(x[j])
    xx.append(g)
    g = []  


xx.append(list("." * (b+1)))    #在最下面一排加上整旁的『.』以防out of index

t = 0

for i in range(a) :
    for j in range(b) :
        if xx[i][j] == "*" :    
            t = t + 1     #遍歷圖形發現第一個『＊』時，矩形計數＋1
            row = i       #以遇到的每個矩形第一個『＊』作為出發點開始尋找該矩形邊界
            line = j
            while xx[row][line] == "*" :  #以遇到的每個矩形第一個『＊』作為出發點開始尋找該矩形邊界
                line = line + 1            #往右找
            line = line -1                #找到該矩形最右邊後，因為目前line代表的座標是『.』退一步回『＊』上

            while xx[row][line] == "*" :   #往下找
                row = row + 1   #####不用檢1 因為沒有要繼續檢查 雖然是錯的(index多1) 但等等要進range又要加1所以不用動#######

            for kk in range(i,row) :     #將剛剛遍歷的『＊』都變成『.』
                for pp in range(j,line+1) :
                    xx[kk][pp] = "."
     
print(t)


