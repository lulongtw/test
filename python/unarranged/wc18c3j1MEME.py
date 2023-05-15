# 總共有P升油漆
# 一個徽章要用B升油漆
# 每枚徽章可以賣D塊
# 剩下每升油漆賣1塊
# 給PBD問賺多少

p = int(input())
b = int(input())
d = int(input())

money = (p // b * d) + (p % b)
print(money)