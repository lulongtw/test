# 畫了一個n高m寬的圖 用 . and * 組成
# * 組成不重疊的矩形 且邊角不會接觸
#算有多少矩形
#input
# n m
# 每n行有m個字母
#靠北怎麼搞

########################不是找矩形#####################
########是找矩形的左上跟右下##################
##################題目設計有問題##################


x = input().split()
n = int(x[0])
m = int(x[1])

grid = []

for i in range(n) :
    grid.append(list(input() + ".")) #list(input) =>["a","b"] 而 [input] = ["ab"]
    if i == n - 1 :
        grid.append(list("." * (m + 1)))

ret = 0

for nn in range(n) :
    for mm in range(m) :
        if grid[nn][mm] == "*" :#找*一找到就算一個ret
            ret = ret + 1
            r = mm
            for ii in range(m) :  #開始往右找*號的邊邊
                if grid[nn][r] == "*" :
                    r = r + 1      #r是以*號往右+1步進找*
                else :
                    d = nn + 1      #如果遇到.則往下找* d是nn+1目前的下一行
                    for iii in range(n) :
                        if grid[d][r -1] == "*" :
                            d = d + 1  #往下找星  
                        else :           #最後矩形的右下點grid[d-1][r-1]被找到  
                            for iiii in range(nn,d) :     #把從這個迴圈開始的*號左上grid[nn][mm]
                                for iiiii in range(mm,r) :#到右下grid[d-1][r-1]形成的矩形的內部*號都刪除
                                    grid[iiii][iiiii] = "."# = == 我的天 m mm幹

print(ret)