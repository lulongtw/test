# 從頭到尾檢查輸入字元
# 要組成HONI
# 只能按照順序組
# 輸出有幾個HONI

x = input().lower()

cha = "honi"
ind = 0
p = 0
for i in range(len(x)) :
    if x[i] == cha[ind] :
        ind = ind + 1
    if ind == 4 :
        ind = 0
        p = p + 1
print(p)

    


