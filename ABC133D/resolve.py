
def resolve():
    '''
    code here
    '''

    N = int(input())
    As = [int(item) for item in input().split()]

    def cal(num):
        last_num = 0
        ans_list = [0 for _ in range(N)]
        
        for i in range(N):
            if i == 0:
                last_num = num // 2
                prev_num = num // 2
                ans_list[0] = num
                continue
            
            temp_num = 2 * (As[i-1] - prev_num)
            ans_list[i] = temp_num
            if temp_num < 0:
                return 'too small'
            
            if i == N-1:
                if last_num + temp_num // 2 == As[-1]:
                    return ans_list
                else:
                    return 'too large'

            prev_num = temp_num //2

    R = 2 * max(As[0], As[-1])
    L = 0
    mid = (R + L)//2
    is_search = True
    while is_search:
        flag = cal(mid)
        if flag == 'too large':
            R, mid = mid, ((L+mid)//4)*2
        elif flag == 'too small':
            L, mid = mid, ((R+mid)//4)*2
        else:
            is_search = False

    print(*flag)

if __name__ == "__main__":
    resolve()
