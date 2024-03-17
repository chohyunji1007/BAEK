N = int(input())
def winning_player(N):
    # 돌이 N개일 때 승리자를 계산하는 함수
    # dp[i]는 돌이 i개일 때 승리자를 나타냄 (0: 창영, 1: 상근)
    dp = [0] * (N + 1)
    dp[1] = 1  # 돌이 1개일 때 상근이가 승리

    # 동적 프로그래밍을 통해 승리자를 계산
    for i in range(2, N + 1):
        # 창영이가 돌을 가져가면 승리
        if dp[i - 1] == 0 or (i >= 3 and dp[i - 3] == 0) or (i >= 4 and dp[i - 4] == 0):
            dp[i] = 1

    return "SK" if dp[N] == 1 else "CY"

# 승리자 출력
print(winning_player(N))