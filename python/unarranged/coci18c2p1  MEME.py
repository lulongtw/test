# 半場得多少分 2x12x60秒時
# 有幾次領先交換

ap = int(input())
ascore = []
for i in range(ap) :
    ascore.append(int(input()))

bp = int(input())
bscore = []
for i in range(bp) :
    bscore.append(int(input()))

def halfscore(a,b) :
    half = 0
    for i in b :
        a.append(i)
    a.sort()
    for i in a :
        if i <= 1440 :
            half = half + 1
    return half

print(halfscore(ascore,bscore))

def fulltimescore(team) :
    fts = [0]
    count = 0
    for i in range(1,2881) :
        if i == team[count] :
            count = count + 1
            if count == len(team) :
                count = count - 1
            fts.append(fts[i-1]+ 1)
        else :
            fts.append(fts[i-1])
    return fts

at = fulltimescore(ascore)
bt = fulltimescore(bscore)

def lead(a,b) :
    lead = ["."]
    for i in range(1,2881) :
        if a[i] > b[i] :
            lead.append("a")
        elif b[i] > a[i] :
            lead.append("b")
        else :
            lead.append(lead[i-1])
    return lead
        


le = lead(at,bt)
ta = 0
for i in range(2881) :
    if at[i] > bt[i] and le[i-1] != "a" :
        ta = ta + 1
    elif bt[i] > at[i] and le[i-1] != "b" :
        ta = ta + 1

print(ta-1)


        
