n = int(input())

desks = []
for i in range(n) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    desks.append(x)


def cmb(dsks,grd) :
    cmbo = 0
    mxcmb = 0
    for dsk in dsks :
        if grd in dsk :
            cmbo = cmbo + 1
            if cmbo > mxcmb :
                mxcmb = cmbo
        else :
            cmbo = 0
    return mxcmb

maxx = 0
ans = []
for i in range(1,6) :
    combo  = cmb(desks,i)
    if combo > maxx :
        maxx = combo
        ans = [str(maxx),str(i)]

print(" ".join(ans))


