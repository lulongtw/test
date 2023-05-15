# 判別是音文還加拿大文
# 如果超過4 個字  字尾是子音+OR 英文  
# 把它換成加拿大文 字尾仔音加OUR 
# Y是母音
#quit退出成˙是


while True :
    x = input()
    if x == "quit" :
        break
    elif (x[-3] not in "aeiouy") and (x[-2:] == "or") and(len(x) > 4) :
        x = x[:-2] + "our"
    print(x)
    
