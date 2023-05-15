# 搶魔障比賽
# 誰贏誰就有魔障
# 輸入
# 第一行是起始擁有者
# 第二航是n場戰鬥
# 下n行是戰鬥內容
# 第一個位置是贏家
# 第二個位置是輸家

# 輸出
# 魔障最後是誰的
# 給幾個不同人有過

# w = input()
# n = int(input())
# c = [w]

# for i in (range(n)) :
#     b = input().split()
#     if w == b[1] :
#         w = b[0]
#         if b[0] not in c:
#             c.append(b[0])

# print(w,len(c))

w = input()
n = int(input())
c = w

for i in (range(n)) :
    b = input().split()
    if w == b[1] :
        w = b[0]
        if b[0] not in c:
            c = c + b[0]
print(w,len(c))