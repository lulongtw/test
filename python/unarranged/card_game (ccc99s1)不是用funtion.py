a = 0
b = 0
dic = {"jack":1,"queen":2,"king":3,"ace":4}
deck = []
# player = {"a":0,"b":0}
for i in range(52) :
    deck.append(input())

i = 0
while i != 52 :
    if i % 2 == 0 :        
        add = ""
        if deck[i] in dic and 51 - i >= dic[deck[i]]:
            for k in range(i+1,i+dic[deck[i]] + 1) :
                if deck[k] in dic :
                    add = "no"
            if add != "no" :
                a = a +  dic[deck[i]]
                print(f"player b scores {dic[deck[i]]} points")
        
        
    else :
        add = ""
        if deck[i] in dic and 51 - i >= dic[deck[i]]:
            for k in range(i+1,i+dic[deck[i]] + 1) :
                if deck[k] in dic :
                    add = "no"
            if add != "no" :
                b = b +  dic[deck[i]]
                print(f"player b scores {dic[deck[i]]} points")

    i = i + 1
print(a)
print(b)