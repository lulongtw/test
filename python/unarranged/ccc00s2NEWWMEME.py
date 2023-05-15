ini = int(input())
num = []

for i in range(ini) :
    num.append(int(input())) #每次都忘記可以直接append進[] 都會在上面開個s = int(input())

while True :
    x = int(input())
    if x == 77 :
        res = ""
        for kk  in range(len(num)) :  #又忘記家rangelen
            res = res + str(num[kk]) + " "
        print(res[:-1])
        break
    elif x == 99 :
        spn = int(input()) -1 #幹真的很賤ㄟ  這個編號跟py的編號不一樣
        spp = int(input())
        left = round(num[spn] * spp / 100)
        num = num[:spn] + [left,num[spn]-left] + num[spn+1:]  #到底要pop還remove  結果不用? 
    elif x == 88 :                                            #思考到到幾怎把r跟l加進去 用:切片把舊的分成兩半?
        spj = int(input()) -1                                 # 可以直接[left,right]不用創left = []再append 
        num = num[:spj] + [num[spj] + num[spj+1]] + num[spj+2:]