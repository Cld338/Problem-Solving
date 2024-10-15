import sys
input=sys.stdin.readline
t=int(input())
while t:
    t=t-1
    ls = []
    i=0
    for i in range(len(bin(t))-2):
        if t&(1<<i):
            ls.append(3**i)
        i+=1
    print("{ " + ", ".join(map(str, ls))+ " }" if t else "{ }")
    t = int(input())