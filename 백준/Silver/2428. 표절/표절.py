N = int(input())
files = sorted(list(map(int, input().split())))
def lower_bound(ls, value):
    left, right = 0, len(ls) - 1
    while left <= right:
        mid = (left + right) // 2
        if ls[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1
    return left
s=0
for i in range(N):
    start_idx = lower_bound(files, files[i]*0.9)
    if start_idx!=-1 and i!=start_idx:
        s+=i - start_idx
print(s)