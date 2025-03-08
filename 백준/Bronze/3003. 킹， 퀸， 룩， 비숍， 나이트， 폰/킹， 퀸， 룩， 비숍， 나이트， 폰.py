ls = list(map(int, input().split()))
ans = [1, 1, 2, 2, 2, 8]
print(" ".join([str(ans[i] - ls[i]) for i in range(6)]))