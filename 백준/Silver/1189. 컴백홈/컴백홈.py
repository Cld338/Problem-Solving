R, C, K = map(int, input().split())
dp = [[0] * C for _ in range(R)]
for r in range(R):
    row = list(input())
    for c in range(C):
        if row[c] == "T":
            dp[r][c] = -1

count = 0

def dfs(visited, d, last):
    global count
    # 도착 조건
    if last == (0, C-1) and d == K-1:
        count += 1
        return
    
    # 탐색 종료 조건
    if d >= K:
        return

    # 상하좌우 탐색
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = last[0] + dr, last[1] + dc
        if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and dp[nr][nc] != -1:
            dfs(visited | {(nr, nc)}, d + 1, (nr, nc))

dfs({(R-1, 0)}, 0, (R-1, 0))
print(count)
