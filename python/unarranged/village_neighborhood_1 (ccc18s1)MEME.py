#o測試ok後看解答縮短優化的顆顆 幹你媽超短超屌 12行
#要改進的就是range




#本來是range(n-1)下面用if跳掉i = 0會造成的錯誤



n = int(input())
x = []
for i in range(n) :
    x.append(int(input()))
x.sort()
z = []
for i in range(1,n-1) :
    left = x[i] - x[i-1]
    right = x[i+1] - x[i]
    t = (left + right) / 2
    z.append(t)
print(min(z))