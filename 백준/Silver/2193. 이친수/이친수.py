N = int(input())
a=0
b=1
for i in range(2,N):
    a,b=b,a+b
print(a+b)