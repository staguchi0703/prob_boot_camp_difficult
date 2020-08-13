def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    As.sort()
    max_num = max(As)

    res = 10**9 + 1
    if max_num % 2 == 0:
        if max_num //2 in As:
            res = max_num //2
        else:
            for item in As:
                if abs(max_num //2 - res) > abs(max_num //2 - item):
                    res = item
    else:
        if max_num //2 in As:
            res = max_num //2
        elif max_num // 2 + 1 in As:
            res = max_num //2 + 1 
        else:
            for item in As:
                if abs(max_num //2 - res) > abs(max_num //2 - item):
                    res = item
                if abs(max_num //2 + 1 - res) > abs(max_num //2 + 1 - item):
                    res = item


    print(max(As), res)

if __name__ == "__main__":
    resolve()
