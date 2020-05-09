def resolve():
    '''
    code here
    '''
    N, A, B = [int(item) for item in input().split()]
    X_list = [int(item) for item in input().split()]

    memo = 0

    for i in range(N-1):
        w_cost = A * (X_list[i+1] - X_list[i])
        memo = min(memo + w_cost, memo + B)       
    
    print(memo)

if __name__ == "__main__":
    resolve()
