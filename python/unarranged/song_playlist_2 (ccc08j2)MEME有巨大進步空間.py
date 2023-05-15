
# Initially, the C3MP playlist is "A, B, C, D, E"

# Button 1    "A, B, C, D, E" will change to "B, C, D, E, A".
# Button 2     "A, B, C, D, E" will change to "E, A, B, C, D".
# Button 3      "A, B, C, D, E" will change to "B, A, C, D, E".
# Button 4   QUIT

# input
# 奇數行是按鈕
# 偶數行是按鈕次數
 
# 輸出歌曲最後長怎樣

s = "abcde"
b = ""

while b != "4" :
    b = input()
    if b == "1" :
        t = int(input())
        for i in range(t) :
            s = s[1:] + s[0]
    elif b == "2" :
        t = int(input())
        for i in range(t) :
            s = s[-1] + s[:-1]
    elif b == "3" :
        t = int(input())
        for i in range(t) :
            s = s[1] + s[0] + s[2:]
    elif b == "4" :
        x = input()

print(s)


