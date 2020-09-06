from prompt_toolkit.filters.app import is_searching


def resolve():
    '''
    code here
    '''

    N = int(input())
    As = [int(item) for item in input().split()]

    def cal(num):
        res_list = [0 for _ in range(N)]
        ans_list = [0 for _ in range(N)]
        
        for i in range(N):
            if i == 0:
                res_list[0] = num // 2
                res_list[-1] = num // 2
                ans_list[0] = num
                continue
            
            temp_num = 2 * (As[i-1] - res_list[i-1])
            ans_list[i] = temp_num
            if temp_num < 0:
                return 'too large'
            
            if i == N-1:
                if res_list[-1] + temp_num // 2 == As[-1]:
                    return ans_list
                else:
                    return 'too small'

            res_list[i-1] += temp_num // 2
            res_list[i] = temp_num //2

    R = 2 * max(As[0], As[-1])
    L = 0
    mid = (R + L)//2
    is_search = True
    while is_search:
        print(mid)
        flag = cal(mid)
        print(flag)
        if flag == 'too large':
            R, mid = mid, (L+mid)//2
        elif flag == 'too small':
            L, mid = mid, (R+mid)//2
        else:
            is_search = False

    print(*flag)

if __name__ == "__main__":
    resolve()
