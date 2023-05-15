# 一球三杯
# 輸入移動動作
# 輸出求最後在哪

p = 1
x = input()

for i in range(len(x)) :
    if x[i] == "A" and p == 1 :
        p = 2
    elif x[i] == "A" and p == 2 :
        p = 1
    elif x[i] == "B" and p == 2 :
        p = 3
    elif x[i] == "B" and p == 3 :
        p = 2
    elif x[i] == "C" and p == 1 :
        p = 3
    elif x[i] == "C" and p == 3 :
        p = 1
print(p)