def resolve():
    '''
    code here
    '''
    N = int(input())
    Ss = [input() for _ in range(N)]

    num_ab = 0
    num_a = 0
    num_b = 0
    num_b_a = 0

    for line in Ss:

        num_ab += line.count('AB')
        if line[0] == 'B' and line[-1] == 'A':
            num_b_a += 1
        elif line[-1] == 'A':
            num_a += 1
        elif line[0] == 'B':
            num_b += 1
        
    res = num_ab
    if num_b_a > 0:
        res += num_b_a -1

        if num_a > 0:
            res += 1
            num_a -= 1

        if num_b > 0:
            res += 1
            num_b -= 1

    res += min(num_a, num_b)
    print(res)


if __name__ == "__main__":
    resolve()
