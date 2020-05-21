def resolve():
    '''
    code here
    '''
    S_dash = input()[::-1]
    T = input()[::-1]

    is_flag = False

    res = ''

    for i in range(len(S_dash)):
        res = S_dash[:i]
        # print(res)
        if len(S_dash) - len(res) >= len(T):
            for j in range(len(T)):
                if S_dash[i+j] == T[j] or S_dash[i+j] == '?':
                    res += T[j]
                else:
                    # print('bk')
                    break
            else:
                is_flag = True
                break

        # print(res)

    # print(S_dash, T, res)
    # print(S_dash[len(T):])
    res = res + S_dash[len(T)+i:]
    res = res.replace('?','a')

    print(res[::-1]) if is_flag else print('UNRESTORABLE')     

if __name__ == "__main__":
    resolve()
