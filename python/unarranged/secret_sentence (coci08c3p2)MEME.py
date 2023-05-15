x = input()

i = 0
ans = ""

while i != len(x) :
    if x[i] in "aeiou" :
        ans = ans + x[i]
        i = i + 3
    else :
        ans = ans + x[i]
        i = i + 1

print(ans)
    
