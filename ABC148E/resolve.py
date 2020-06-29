def resolve():
    '''
    code here
    '''
    N = input()

    res = 0
    if int(str(N)[-1]) % 2 == 0:
        i = 0
        N=int(N)
        while int(N) >= 2*5**i:
            i += 1
            res += N//(2*5**i)

    print(res)



if __name__ == "__main__":
    resolve()
