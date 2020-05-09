def resolve():
    '''
    code here
    '''
    S = int(input())

    a, b = divmod(S, 10**9)
    x2 = (10**9 - b)%10**9
    y2 = (S+x2) // (10**9)

    print(0,0, 10**9, 1, x2, y2)

if __name__ == "__main__":
    resolve()
