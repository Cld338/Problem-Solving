import sys

def solve():
    input = sys.stdin.readline
    
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        
        # DP 배열 초기화
        if N == 1:
            print(max(stickers[0][0], stickers[1][0]))
            continue
        
        dp = [[0] * N for _ in range(2)]
        
        # 초기값 설정
        dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
        dp[0][1], dp[1][1] = stickers[1][0] + stickers[0][1], stickers[0][0] + stickers[1][1]
        
        if N == 2:
            print(max(dp[0][1], dp[1][1]))
            continue
        
        # DP 점화식 적용
        for i in range(2, N):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]
        
        # 최댓값 출력
        print(max(dp[0][-1], dp[1][-1]))

if __name__ == "__main__":
    solve()
