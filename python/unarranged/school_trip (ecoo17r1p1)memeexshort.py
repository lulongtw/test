x = int(input())

v = []
for i in range(x) :
    v.append(int(input()))
v.sort()

min = 999999

for i in range(1,x - 1) :
    right = (v[i] - v[i-1]) / 2
    left = (v[i + 1] - v[i]) / 2
    print(right + left)
    if right + left <= min :
        min = right + left

print(min)