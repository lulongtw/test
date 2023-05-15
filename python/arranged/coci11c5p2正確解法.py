"""
題目給定n顆樹木的高度跟目標採收量，詢問樹木最高應留高度要設多少，
採伐下來的樹木才會剛好是目標採收量，
會先從最高的樹開始採收，如果低於最高應留高度就忽略不理
"""


x = input().split()
n = int(x[0])
requried = int(x[1])

trees = input().split()
for i in range(n) :
    trees[i] = int(trees[i])

trees.sort()   ##排序大小 之後要從高的開始砍

total = 0
i = n - 2    ##將i設為倒數第二個


while total < requried :  
    cutted = trees[i+1] - trees[i]   #一開始以第二高的樹為標準開始砍 接著第三高，依序砍下去 
    tree_cutted = n - i - 1          #紀錄被砍的數有幾顆
    total = total + cutted * tree_cutted    #加總砍下來的數目
    i = i - 1                    #追蹤下一顆高的樹


add = 0
if total > requried : 
    superfluous = total - requried     #確定多砍的數量
    add = superfluous // (n-i-2)    #講這些多砍的量平均分給被砍過的樹 


print(trees[i+1]+ add)    #在把平均多砍的量加上最後一顆被當作被當標準的樹高就是答案