def resolve():
    '''
    code here
    累積和は単調増加だから二分探索できる。
    '''
    N, K = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]

    memo = [0]
    for i in range(N):
        memo.append(memo[-1]+As[i])


    res = 0
    for i in range(N):
        if memo[-1] - memo[i] < K:
            continue
        
        left, right = i, N
        while abs(left - right) > 1:
            mid = (left + right)//2
            if memo[mid] - memo[i] >= K:
                right = mid
            else:
                left = mid
        res += N - left
    print(res)


if __name__ == "__main__":
    resolve()
