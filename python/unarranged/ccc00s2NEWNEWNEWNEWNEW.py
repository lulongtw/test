n = int(input())
f = []

for i in range(n) :
    f.append(int(input()))

while True :
    x = input()
    if x == "77" :
        break
    elif x == "99" :
        num = int(input()) - 1
        left = f[num] * int(input()) // 100
        right = f[num] - left
        f.remove(f[num])
        f.insert(num,right)
        f.insert(num,left)
    elif x == "88" :
        num = int(input()) - 1
        x = f[num+1]
        f.remove(f[num+1])
        f[num] = f[num] + x

print(f)
