def resolve():
    '''
    code here
    '''
    S = input()
    dp0 = [1 for _ in range(len(S))]
    dp1 = [0 for _ in range(len(S))]

    K = 10**5
    bit_k = bin(K)[2:]

    # print(bit_k)

    for j in range(len(S)):
        if S[j] == 'L':
            dp1[j-1] += dp0[j]
        if S[j] == 'R':
            dp1[j+1] += dp0[j]

    dp = [[0 for _ in range(len(S))] for _ in range(len(bit_k)+1)]
    dp[0] = dp1

    for i in range(len(bit_k)):
        for j in range(len(S)):
            if S[j] == 'L':
                if dp[i][j] >= 1:
                    dp[i+1][j-1] += dp[i][j]
            if S[j] == 'R':
                if dp[i][j] >= 1:
                    dp[i+1][j+1] += dp[i][j]

    # print(dp)
    res = [[0 for _ in range(len(S))] for i in range(len(bit_k))]


    for i in range(len(bit_k)):
        if ((K >> i) & 1):
            for j in range(len(S)):
                if S[j] == 'L':
                    if dp[i][j] >= 1:
                        res[i][j-1] += dp[i][j]
                if S[j] == 'R':
                    if dp[i][j] >= 1:
                        res[i][j+1] += dp[i][j]

    print(*res[-1])

if __name__ == "__main__":
    resolve()
