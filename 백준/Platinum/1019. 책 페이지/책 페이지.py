d=[0 for _ in range(10)]
n=input()
k=len(n)
for x in n:
    k-=1
    for i in range(int(x)):
        d[i]+=10**k
        for j in range(10):
            if k>=1:
                d[j]+=(10**(k-1))*k
    d[0]-=10**k
    if k:
        d[int(x)]+=(int(''.join(n[-k:]))+1)
    else:
        d[int(x)]+=1
print(*d)