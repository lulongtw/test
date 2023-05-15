x = input().split()
n = int(x[0])
requried = int(x[1])

trees = input().split()
for i in range(n) :
    trees[i] = int(trees[i])

# #這這樣的 他用第二高的樹當作標準下去砍 砍下來的就是cutted  放到total 內 此時第一次回圈被砍的只有第一高的樹 所以乘以1
#  第二次迴圈就輪到第三個大的為標準  所以是 第一次迴圈的cutted 加上以第三高圍標準砍下來的cutted 再乘以2  然後加總 因為這樣才是以
# 第三科高的為標準得到的cutted  一直球道 total >= requried  跳出迴圈時i已經被多扣1 所以trees[i+1]才是脫出迴圈時 作為標準的樹
# 此時total如果是大於requ的情況  要把多出來量的除以已經被砍掉的樹數目  再加上標準高trees[i+1]  
# 為什麼要除以已經被砍掉的樹數目哩  因為要把這些多出來的數量平均返回給那些被砍過的樹  才能讓total = requried
然後下方是我用二元搜尋法抱裡找出  太慢幹

trees.sort()

total = 0
i = n - 2

while total < requried :
    cutted = trees[i+1] - trees[i]
    tree_cutted = n - i - 1
    total = total + cutted * tree_cutted 
    i = i - 1



add = 0
if total > requried :
    superfluous = total - requried
    add = superfluous // (n-i-2)

print(trees[i+1]+ add)



# import sys
# input = sys.stdin.readline


# x = input().split()
# n = int(x[0])
# r = int(x[1]) 

# tree = input().split()
# for i in range(n) :
#     tree[i] = int(tree[i])


# def chop(hght,tre) :
#     total = 0
#     for i in range(len(tre)) :
#         if tre[i] > hght :
#             total = total + tre[i] - hght
#     return total


# hight = max(tree)
# y = max(tree)
# finded = False

# while not finded :

#     y = y //2
#     if y < 1 :
#         y = 1

#     harvst = chop(hight,tree)
#     if harvst == r :
#         finded = True

#     elif harvst < r :
#         hight = hight - y
    
#     elif harvst > r :
#         hight = hight + y


# print(hight)
