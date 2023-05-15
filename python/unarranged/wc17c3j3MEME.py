# 搞密碼
# 密碼介於8~12字母長
# 每個字母都是大小寫英文字母或者數字
# 小寫最少3個  大寫最少2個   最少1個數字
# 輸出valid或invalid

x = input()
u = 0
l = 0
d = 0

for i in range(len(x)) :
    if x[i].isupper() == True :
        u = u + 1
    elif x[i].islower() == True :
        l = l + 1
    elif x[i] in "01234567890" :
        d = d + 1


print(u,l,d)

if ((len(x) >= 8 and 12 >= len(x)) 
and u >= 2 and l >= 3 and d >= 1) :
    print("valid")
else :
    print("invalid")