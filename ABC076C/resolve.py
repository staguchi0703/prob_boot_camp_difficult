def resolve():
    '''
    code here
    '''
    S_dash = input()
    T = input()

    is_flag = False

    res = ''
    res_list = ['zzzzz']
    for i in range(len(S_dash) - len(T) +1):
        res = S_dash[:i]
        # print(i, res)
        if len(S_dash) - len(res) >= len(T):
            for j in range(len(T)):
                if S_dash[i+j] == T[j] or S_dash[i+j] == '?':
                    res += T[j]
                else:
                    # print('bk')
                    break
            else:
                is_flag = True
                res += S_dash[i+len(T):]
                res_list.append(res)


    # print(res_list)

    res2_list = []
    for res in res_list:
        res = res.replace('?','a')
        res2_list.append(res)

    res2_list.sort()
    res = res2_list[0]

    print(res) if is_flag else print('UNRESTORABLE')     

if __name__ == "__main__":
    resolve()
