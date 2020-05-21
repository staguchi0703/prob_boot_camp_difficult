def resolve():
    '''
    code here
    '''
    a, b, x = [int(item) for item in input().split()]
    _a = a // x
    _b = b // x

    if a % x == 0:
        res = _b - _a + 1
    else:
        res = _b - _a
    
    print(res)



if __name__ == "__main__":
    resolve()
