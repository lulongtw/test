x = input().split()
row = int(x[0])
col = int(x[1])

setr = set()
setc = set()
    
for i in range(row) :
    x = input()
    while x != "." * col :
        setr.add(i)
        ind = x.index("X")
        setc.add(ind)
        x = x[:ind] + "." + x[ind+1:]

n = int(input())
for i in range(n) :
    x = input().split()
    seer = int(x[1]) -1
    seec = int(x[0]) -1
    if seer in setr or seec in setc :
        print("Y")
    else :
        print("N")