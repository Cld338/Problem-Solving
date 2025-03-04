import sys
input = sys.stdin.readline
S = sum([int(input()) for i in range(4)])
print(S//60)
print(S%60)