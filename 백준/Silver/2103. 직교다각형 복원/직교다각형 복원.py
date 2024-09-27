N = int(input())

vX = [[] for _ in range(10001)]
vY = [[] for _ in range(10001)]

for _ in range(N):
    x, y = map(int, input().split())
    vX[x].append(y)
    vY[y].append(x)

sum = 0
for i in range(10001):
    vX[i].sort()
    vY[i].sort()

    for j in range(0, len(vX[i]), 2):
        sum += vX[i][j+1] - vX[i][j]
    for j in range(0, len(vY[i]), 2):
        sum += vY[i][j+1] - vY[i][j]

print(sum)