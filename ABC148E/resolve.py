def resolve():
    '''
    code here
    '''
    N = int(input())

    res = 0
    if int(N[-1]) % 2 == 0:
        divisor = 1

        while divisor <= N:
            res += N

    print(res)



if __name__ == "__main__":
    resolve()
