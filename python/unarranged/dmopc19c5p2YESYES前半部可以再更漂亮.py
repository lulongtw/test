x = input().split()
n = int(x[0])
h = int(x[1])

chaly = []
for i in range(n) :
    s = input().split()
    s[1] = int(s[1])
    chaly.append(s)

bot = []
for i in range(n) :
    s = input().split()
    s[1] = int(s[1])
    bot.append(s)

d = 0
for i in range(n) :
    bot.insert(d,chaly[i])
    d = d + 2

bot.append(["."]*2)
bot.insert(0,[".","s"])

# print(bot)



chp = h
bhp = h
i = 1

while chp != 0 and bhp != 0 and i != n * 2 + 1:
#####################################
  ##下面兩個IF註解掉是因為 當初想用前兩個IF過濾掉I=0和I=1 
  #然後後面用ELIF繼續計算 但i = 0時 處理完第一個if 雖然不會進入第二個if
  #但會因為地2個IF沒有成立而考慮進入第2個if下的elif  依但符合條件就會進入
  #所以乾脆前面直接加假資料來規避i-1會out of index的情況
#####################################
    # if i == 0 and bot[i][0] == "A" :
    #     bhp = bhp - bot[i][1]
    #     print(bhp)
 
    # if i == 1 and bot[i][0] == "A" and bot[i-1][0] != "D" :
    #     chp = chp - bot[i][1]
    #     # print(chp)
    
    if i % 2 == 1 :
        if bot[i][0] == "A" and bot[i-1][0] != "D" :
            bhp = bhp - bot[i][1]
            # print(bhp)
            # print(bot[i][1])
            # print(i)
        elif bot[i][0] == "D" and bot[i+1][0] != "A" :
            chp = chp - bot[i][1]
            # print(chp)
    elif i % 2 == 0  :
        if bot[i][0] == "A" and bot[i-1][0] != "D" :
            chp = chp - bot[i][1]
            # print(chp)
        elif bot[i][0] == "D" and bot[i+1][0] != "A" :
            bhp = bhp - bot[i][1]
            # print(bhp)
    i = i + 1



if chp>0 and bhp==0 :
    print("VICTORY")
elif chp >0 and bhp >0 :
    print("TIE")
else :
    print("DEFETE")
