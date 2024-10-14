n, k = map(int,input().split())
res = 0
while bin(n).count('1') > k:
    loc = bin(n)[::-1].index('1')
    res += 2 ** loc
    n += 2 ** loc
print(res)