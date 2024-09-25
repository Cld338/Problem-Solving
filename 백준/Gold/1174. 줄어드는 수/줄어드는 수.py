queue=[i for i in range(10)]
next_queue = []
a=int(input())
n=0
while True:
    if not(queue):
        queue=next_queue
        next_queue=[]
    if not(queue):
        print(-1)
        break
    x = queue.pop(0)
    n+=1
    if n==a:
        print(x)
        break
    for i in range(x%10):
        next_queue.append(10*x+i)