def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    D = [int(item) for item in input().split()]
    d_dict = collections.Counter(D)
    print(D)
    print(d_dict)
    cnt = 0
    if D[0] != 0 and D.count(0) != 1:
        pass
    else:
        cnt = 1
        for i in D[1:]:
            if i >0 :
                cnt *= d_dict[i-1]
                print(d_dict[i-1])

            cnt %= 998244353

            print(cnt)
            print('---')

    print(cnt)

if __name__ == "__main__":
    resolve()
