#  範例中將把platform集合sort後 最大的y的集合開始檢查
#  如果有不同的y隊裡相同的x點  分別是頭跟尾 則跳過檢查該x點 def
#  檢查其x點是否夾在y更小的x集合區區間內，如果有，該y更小的集合區間加入z[]， def
#  如果是夾在一個以上的區間十，取y最大的那個 注意不能往y值更大的x集合區間內找
#  將所有y集合加總*2再減掉z總和

n = int(input())
p = []
for i in range(n) :
    g = input().split()
    for j in range(len(g)) :
        g[j] = int(g[j])
        if j == 1 :
            g[j] = g[j] + 0.5
        elif j == 2 :
            g[j] = g[j] - 0.5
    p.append(g)

p.sort(reverse = True)

point = 0
for k in range(1,3) :
    i = 0
    while i < (len(p)-1) :
        for j in range(i+1,len(p)) :
            if p[i][k] >= p[j][1]  and p[i][k] <= p[j][2]  :
                point = point + p[j][0]
                break
        i = i + 1

print(point)