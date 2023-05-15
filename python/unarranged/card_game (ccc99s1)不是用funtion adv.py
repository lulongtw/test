dic = {"jack":1,"queen":2,"king":3,"ace":4}
deck = []
player = {0:0,1:0}
for i in range(52) :
    deck.append(input())

i = 0
while i != 52 :     
    add = ""
    if deck[i] in dic and 51 - i >= dic[deck[i]]:
        for k in range(i+1,i+dic[deck[i]] + 1) :
            if deck[k] in dic :
                add = "no"
        if add != "no" :
            player[i%2] = player[i%2] +  dic[deck[i]]
            if i%2 == 0 :
                pl ="A"
            else :
                pl = "B"
            print(f"Player {pl} scores {dic[deck[i]]} point(s).")
    i = i + 1
print(f"Player A: {player[0]} point(s).")
print(f"Player A: {player[1]} point(s).")
