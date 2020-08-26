def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]
    As.sort()
    res = 1
    remain = sum(As)

    for i in range(N-1):
        temp = As[-1 * (i + 1)]
        remain -= temp

        if temp <= remain * 2:
            res += 1
        else:
            break

    print(res)


if __name__ == "__main__":
    resolve()
