from math import gcd
from collections import defaultdict

n = int(input())
original = [tuple(map(int, input().split())) for _ in range(n)]
tot = 0

def calc(center):
    global tot
    M = defaultdict(int)
    for i in range(n):
        if i == center:
            continue
        tx = original[i][0] - original[center][0]
        ty = original[i][1] - original[center][1]
        g = gcd(tx, ty)
        if g < 0:
            g = -g
        tx //= g
        ty //= g
        M[(tx, ty)] += 1
    
    for (x, y), count in M.items():
        if (-y, x) in M:
            tot += count * M[(-y, x)]

for i in range(n):
    calc(i)

print(tot)
