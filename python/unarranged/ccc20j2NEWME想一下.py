p = int(input())
n = int(input())
r = int(input())
d = 0
total = n

while total <= p :
    d = d + 1
    v = n * (r**d)
    total =  total + v 

print(total)
print(d)