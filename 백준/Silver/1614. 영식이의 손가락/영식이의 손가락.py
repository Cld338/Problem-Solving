n=int(input())
m=int(input())
if n==1:k=8*m
elif n==5:k=8*m+4
elif m%2==1:k=5-n+4*m
else:k=n-1+4*m
print(k)