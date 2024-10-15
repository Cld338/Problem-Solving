import sys
input=sys.stdin.readline
t=int(input())
while t:
    n = bin(t-1)[2:]
    ls = []
    for i in range(len(n)):
        if int(n[i]):
            ls.append(str(3**(len(n)-i-1) * int(n[i])))
    print("{ }" if t==1 else "{ " + ", ".join(ls[::-1])+ " }")
    t = int(input())