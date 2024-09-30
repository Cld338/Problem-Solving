import sys
input = sys.stdin.readline
case_num = int(input())
n = 0

def distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def isUnion(GroupA, GroupB):
    for i in GroupA:
        for j in GroupB:
            if distance(i, j) == 1:
                return 1
    return 0

for _ in range(case_num):
    M, N, K = map(int, input().split())
    coords = [list(map(int, input().split())) for _ in range(K)]
    union = [[coord] for coord in coords]
    n = 0
    i = 0
    j = 1
    if len(union) > 1:
        while True:
            if isUnion(union[i], union[j]):
                union[i] = union[i] + union[j]
                union.pop(j)
                j = i+1
            else:
                j +=1
            if j > len(union) - 1:
                j = 1
                i += 1
            if i > len(union) - 2:
                break
    print(len(union))