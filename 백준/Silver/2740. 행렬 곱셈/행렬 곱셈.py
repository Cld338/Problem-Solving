import sys
N, M = map(int, sys.stdin.readline().split())
array_A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
array_B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
array_AB = []
for i in range(N):
    array_AB.append([])
    for j in range(K):
        S = 0  
        for k in range(M):
            S += array_A[i][k]*array_B[k][j]
        array_AB[-1].append(S)
for arr in array_AB:
    print(" ".join([str(i) for i in arr]))