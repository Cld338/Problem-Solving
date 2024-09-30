from math import sqrt, floor
for i in range(int(input())):
    A,B=map(int, input().split())
    N=B-A
    n=floor(sqrt(N))
    t=2*n-1
    N-=n**2
    for i in range(n,0,-1):
        t+=N//i
        N%=i
    print(t)