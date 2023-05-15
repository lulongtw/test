"""
給定一張圖，圖上有幾個跟蹤怪Ｘ，並給定幾個saki的位置座標，saki的視野只有上下左右的無限遠，
詢問當saki在圖上的那些給定做標時，是否會看到跟蹤怪

"""



import sys
input = sys.stdin.readline

x = input().split()
r = int(x[0])
c = int(x[1])

row = set()
col = set()

for i in range(r) :
    x = input().strip()
    while x != "." * c :  #當輸入不全是『.』時，可以確定該row至少有一個『X』
        row.add(i)        
        col.add(x.index("X"))   #紀錄左邊數來第一個『Ｘ』
        x = x.replace("X",".",1) #把該行的『X』位置都記錄下來，紀錄玩就把左邊數來第一個『Ｘ』變成『.』  


q = int(input())

for i in range(q) :
    x = input().split()
    rr = int(x[1])-1    #題目給定的row 和colume位置相反
    cc = int(x[0]) -1
    if rr in row or cc in col:
        print("Y")

    else :
        print("N")

