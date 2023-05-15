# n是題目數
# 前n行是正卻答案
# 後n行是學生答案
# 看對幾題輸出

x = int(input())
t = ""
for i in range(x) :
    t = t + input()
s = ""
for i in range(x) :
    s = s + input()
p = 0
for i in range(x) :
    if s[i] == t[i] :
        p += 1
print(p)
