def resolve():
    '''
    code here
    '''
    S = input()

    memo = 1
    new_list = []
    prev = S[0]

    for i in range(len(S)-1):
        if S[i+1] == prev:
            memo += 1
        else:
            new_list.append(memo)
            memo = 1
        prev = S[i+1]
    else:
        new_list.append(memo)

    # print(new_list)

    res = []
    for i in range(len(new_list)//2):

        a = new_list[i*2]
        b = new_list[i*2 +1]

        res += [0 for _ in range(a)]
        res[-1] = (a+1)//2 + b//2
        res += [a//2 + (b+1)//2]
        res += [0 for _ in range(b-1)]

    print(*res)


if __name__ == "__main__":
    resolve()
