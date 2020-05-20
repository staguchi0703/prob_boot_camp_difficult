def resolve():
    '''
    code here
    '''
    import collections
    H, W = [int(item) for item in input().split()]

    grid = [[item for item in input()] for _ in range(H)]
    
    dp = [[10**5 for _ in range(W+1)] for _ in range(H+1)]



    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                dp[i][j] = 1
            else:
                dp[i][j] = 0
    
    # print(dp)

    for i in range(H):
        for j in range(W):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+dp[i+1][j])
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+dp[i][j+1])

    print(dp)

if __name__ == "__main__":
    resolve()
