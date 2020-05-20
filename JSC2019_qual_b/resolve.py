def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]

    mod = 10**9+7

    base_n = 0

    for i in range(N):
        for j in range(i+1,N):
            if A_list[i] > A_list[j]:
                base_n += 1
    
    all_n = 0
    for i in range(N):
        for j in range(N):
            if A_list[i] > A_list[j]:
                all_n += 1


    print(((base_n*K)+all_n*(K-1)*K//2)%mod)


if __name__ == "__main__":
    resolve()
