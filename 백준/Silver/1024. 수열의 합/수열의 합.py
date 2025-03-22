N,L=map(int,input().split())
while True:
  if L>100:print(-1);exit()
  k=2*N-L*(L+1)
  if k%(2*L)==0:
    a=k//(2*L)
    if a<-1:print(-1);exit()
    print(" ".join([str(a+i+1) for i in range(L)]));exit()
  else:
    L+=1
