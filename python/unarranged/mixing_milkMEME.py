# # 要拿三個桶子混和三隻牛的奶
# # 桶子可能size不一樣 可能部會裝滿
# 算每次迭代的情形 並記錄下來 直到相同的牛奶容量出現
# 出現後該行牛奶容量及上兩行抓起來 看其中哪個迭代次數是%3 = 1(因為100%3=1) 該行就是答案



# # input_file = open("milk.in","r")
# # write_input = open("milk.in","w")
count = -1
max = []
lst = []
current = []
for i in range(3) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    max.append(x[0])
    current.append(x[1])
    
def first(cur,ma,cou) :
    x = cur[cou%3]   
    y = cur[(cou+1)%3]   
    if x + y > ma[(cou+1)%3]   :
        cur[cou%3] = (x + y) - ma[(cou+1)%3] 
        cur[(cou+1)%3] = ma[(cou+1)%3]
    else :
        cur[cou%3] = 0
        cur[(cou+1)%3] = x + y
    return current



while lst.count(current) != 2 :
    count = (count + 1) % 3
    current = first(current,max,count)
    k = current[:]   
    lst.append(k)  

for i in range(len(lst)-1,-1,-1) :
    if count == 0 :
        print(lst[i])
        break
    count = count -1