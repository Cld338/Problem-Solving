N = int(input())
ls = [input() for _ in range(N)]
ls.sort()
X = 1
curr = ls[0]
for i in range(1, N):
    if curr != ls[i][:len(curr)]:
        X+=1
    curr = ls[i]
print(X)