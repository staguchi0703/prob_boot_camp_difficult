def resolve():
    '''
    code here
    '''
    import collections
    import numpy as np
    H, W = [int(item) for item in input().split()]

    grid = [[item for item in input()] for _ in range(H)]
    dp = [[300 for _ in range(W+1)] for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                if grid[0][0] == '#':
                    dp[i+1][j+1] = 1
                else:
                    dp[i+1][j+1] = 0
            else:
                add_v = 0
                add_h = 0
                if grid[i][j] != grid[i][j-1]:
                    add_h = 1
        
                if grid[i][j] != grid[i-1][j]:
                    add_v = 1

                dp[i+1][j+1] = min(dp[i+1][j]+add_h, dp[i][j+1]+add_v)
    # print(dp)
    if grid[H-1][W-1] == '#':
        print(dp[H][W]//2+1)
    else:
        print(dp[H][W]//2)

if __name__ == "__main__":
    resolve()
