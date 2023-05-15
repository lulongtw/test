n = int(input())
for i in range(n) :
    x = input()
    word = x[0]
    digit = 0
    out = ""

    for j in range(len(x)) :
        if word != x[j] :
            out = out + str(digit) + word
            digit = 0
            word = x[j]
        digit = digit + x[j].count(word)
        if j == len(x) -1 :
            out = out + str(digit) + word
    
    print(out)
        