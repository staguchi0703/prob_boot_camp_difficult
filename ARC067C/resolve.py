def resolve():
    '''
    code here
    '''
    N = int(input())

    def get_sieved_list(x):
        dp = [1 if item % 2 == 0 else 0 for item in range(x+1)]
        dp[:3] = [2,1,1]

        for prim_candi in range(3, x+1):
            temp_num = prim_candi
            while temp_num <= x:
                dp[temp_num] += 1
                temp_num += prim_candi
            if prim_candi >= x:
                return [i  for i in range(x+1) if dp[i] == 1]
                
    
    if N > 2:
        factor_filter = set(get_sieved_list(N))
        prime_list = [0 for _ in range(N+1)]
        for i in factor_filter:
            if i >1:
                for j in range(2, N+1):
                    while j >= 1 and j % i == 0:
                        j //= i
                        prime_list[i] += 1

        res = 1
        for item in prime_list:
            res *= (item+1)
            res %= (10**9+7)
    else:
        res = N

    print(res%(10**9+7))

if __name__ == "__main__":
    resolve()
