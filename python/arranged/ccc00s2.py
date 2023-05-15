"""
題目網址
https://dmoj.ca/problem/ccc00s2
山上有幾道瀑布，給定它們的水量
，當輸入『99』時，代表指定瀑布會分岔，並給定分叉後的支流瀑布大小百分比
輸入88代表指定瀑布會匯流到右邊，輸入『77』印出瀑布分叉匯流後的結果
"""


ini = int(input())
num = []

for i in range(ini) :
    num.append(int(input())) 
while True :
    x = int(input())
    if x == 77 :
        res = ""          
        for kk  in range(len(num)) :  #把答案換成字串 不然沒法過關
            res = res + str(num[kk]) + " "
        print(res[:-1])  #不要印出最後一個空白
        break
    elif x == 99 :
        spn = int(input()) -1 #取得分叉瀑布編號
        spp = int(input())    #取得分叉後的左邊流量百分比
        left = round(num[spn] * spp / 100)
        num = num[:spn] + [left,num[spn]-left] + num[spn+1:]  #編寫新的瀑布們流量
    elif x == 88 :                                            
        spj = int(input()) -1                                 
        num = num[:spj] + [num[spj] + num[spj+1]] + num[spj+2:]
