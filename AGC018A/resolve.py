def resolve():
    '''
    code here
    '''
    import math
    N, K = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]

    gcd = As[0]
    for item in As[1:]:
        gcd = math.gcd(gcd, item)

        
    res = 'IMPOSSIBLE'
    max_A = max(As)
    if max_A > K:
        if K % gcd == 0:
            res = 'POSSIBLE'
    elif K in set(As):
        res = 'POSSIBLE'
    
    print(res)


if __name__ == "__main__":
    resolve()
