n = int(input())
case = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]

for i in range(n) :
    rem = int(input())
    case[rem-1] = 0


if int(input()) > sum(case) // (10-n) :
    print("deal")
else:
    print("no")



    
    
    
