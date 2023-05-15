# 依序玩三台拉霸機
# 每次投一塊
# 第一台投35塊後噴30
# 第一台投100塊後噴60
# 第一台投10塊後噴9

# 輸入
# 身上的錢
# 每台拉霸機剛開始已經投幾塊
# 輸出玩第幾次破產

m = int(input())
a = int(input())
b = int(input())
c = int(input())

i = 0
ma = "abc"

while m - i != 0 :
    i = i + 1
    if ma[i%3] == "a" :
        a = a + 1
        if a % 35 == 0 :
            m = m + 30
    elif ma[i%3] == "b" :
        b = b + 1
        if b % 100 == 0:
            m = m + 60
    elif ma[i%3] == "c" :
        c = c + 1
        if c % 10 == 0 :
            m = m + 9

print(i)


