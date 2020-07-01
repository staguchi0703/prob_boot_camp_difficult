def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    D = [int(item) for item in input().split()]
    d_dict = collections.Counter(D)

    cnt = 0
    if D[0] != 0:
        pass
    else:
        cnt = 1
        for i in D[1:]:
            cnt *= d_dict[i-1]
            cnt %= 998244353


    print(cnt % 998244353)

if __name__ == "__main__":
    resolve()
