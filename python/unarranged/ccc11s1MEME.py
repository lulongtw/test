# 比較T t 和S s哪個誰多
# t 多事英文
# s多或依樣多是法文
# 輸出判斷英法

n = int(input())

t = 0
s = 0
for i in range(n) :
    line = input().lower()
    t = t + line.count("t")
    s = s + line.count("s")

if s >= t :
    print("fran")
else :
    print("eng")


    
