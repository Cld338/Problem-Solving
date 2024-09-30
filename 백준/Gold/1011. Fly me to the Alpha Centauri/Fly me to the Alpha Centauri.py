import sys
input=sys.stdin.readline
for i in range(int(input())):
    A,B=map(int, input().split())
    N=B-A
    n=int(N**.5//1)
    t=2*n-1
    N-=n**2
    print(t+N // n + (0 if N % n == 0 else 1))