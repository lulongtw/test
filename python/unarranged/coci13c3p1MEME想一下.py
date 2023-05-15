# 案神奇按鈕會讓A 變B  B變BA
# 一開始是A
# 問案了K次 A有幾個B有幾歌

##########下面有兩種做法####################



# k = int(input())

# x = 1
# y = 0

# for i in range(k) :
#     x,y = y,x + y
# print(x,y)

k = int(input())

x = 1
y = 0

for i in range(k) :
    a = x
    b = y
    x = b
    y = a + b
print(x,y)