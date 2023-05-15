# 找到文中的tataat後4位之後 裡面藏有答案

# 尋找tataat後4位之後  用while開始以6位為單位往後尋找 假設一開始是

# --------------------------------------------
# tataat 1234 123456789-123456789 先假設1~6是終結子 往後也就是789123的反轉是互補終結子
# 如果 789123不是 在往下推進891234的反轉檢查是不是互補中結子直到結束
# 再換假設234567是終結子 往後891234的反轉檢查是不是互補中結子......
# ---------------------------------------
# 以上框內是舊想法 打出來後有個地方無法解決我也不知道為啥
# 然後參考答案後用了比較簡單的檢查是否in在裡面 就可以知道終結子了


# def檢查 是否是否反轉,互補
# def互補 

# 找到終結子 輸出終結子前 tataat後四位之後 把a改u 其他互補

x = input()

for i in range(len(x)) :
    if x[i:i+6] == "TATAAT" :
        x = x[i+10:]
        break

com = ["G","C","T","A"]
com1 = ["C","G","A","T"]
com2 = ["C","G","A","U"]

def comres(st) : 
    newst = ""
    for i in range(len(st)-1 ,-1,-1) :
        for j in range(4) :
            if st[i] == com[j] :
                newst = newst + com1[j]
                break
    return newst

i = 0
while i < len(x)-5 :
    spt = x[i:i+6]
    serspt = x[i+6:]
    s = comres(spt)
    if s in serspt :
        ans = i
        i = 999999
    else :
        i = i + 1

trans = x[:ans]
fin = ""
for i in range(len(trans)) :
    for j in range(4) :
        if trans[i] == com[j] :
            fin = fin + com2[j]

print(fin)    