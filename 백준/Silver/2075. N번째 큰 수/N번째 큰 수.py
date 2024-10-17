def main():
    import os
    import io
    from heapq import heapify, heapreplace
    input = io.BufferedReader(io.FileIO(0), 1 << 18).readline
    N = int(input())
    A = list(map(int, input().split()))
    heapify(A)
    for _ in range(1, N):
        for x in map(int, input().split()):
            if x > A[0]:
                heapreplace(A, x)
    os.write(1, str(A[0]).encode())
    os._exit(0)
main()