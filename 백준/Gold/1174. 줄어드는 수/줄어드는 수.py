q=list(range(10))
p=[]
a=int(input())
n=0
while True:
    if not(q):
        q,p=p,[]
    if not(q):
        print(-1)
        break
    x=q.pop(0)
    n+=1
    if n==a:
        print(x)
        break
    for i in range(x%10):
        p.append(10*x+i)