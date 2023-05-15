"""
題目給定n顆樹木的高度跟目標採收量，詢問樹木最高應留高度要設多少，
採伐下來的樹木才會剛好是目標採收量，
會先從最高的樹開始採收，如果低於最高應留高度就忽略不理

我很喜歡這個解法，因為是看YT上說明二元搜尋這個概念自己動手做的
而且他不會受限於只有一棵樹的情況，感覺比較泛用，缺點就是太慢無法過關
"""


import sys
input = sys.stdin.readline


x = input().split()
n = int(x[0])
r = int(x[1]) 

tree = input().split()
for i in range(n) :
    tree[i] = int(tree[i])


def chop(hght,tre) :  #以hght為高度標準下去砍樹，高於hght的都砍掉 砍到的部分作為收成
    total = 0
    for i in range(len(tre)) :
        if tre[i] > hght :
            total = total + tre[i] - hght
    return total


hight = max(tree)  #先以最高樹高為標準
y = max(tree)
finded = False

while not finded :

    y = y //2     
    if y < 1 :
        y = 1

    harvst = chop(hight,tree)  
    if harvst == r :
        finded = True

    elif harvst < r :  #收成量太少 則降低高度標準
        hight = hight - y
    
    elif harvst > r :  #收成太多 則提高高度標準
        hight = hight + y


print(hight)
