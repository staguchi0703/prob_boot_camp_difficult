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
    # ３つの関係で解の条件分け
    

    for line in Ss:
        prev = ''
        for j in range(len(line)):
            if prev == 'A' and line[j] == 'B':
                num_ab += 1
            prev = line[j]
        
        if line[0] == 'B' and line[-1] == 'A':
            num_b_a += 1
        elif line[-1] == 'A':
            num_a += 1
        elif line[0] == 'B':
            num_b += 1
        
    if num_a > num_b:
        res = num_ab
        res += num_b
        delta = num_a - num_b
        res += min(num_b_a, delta)
        if num_b_a > delta:
            res += num_b_a - delta
        
    else:
        res = num_ab
        res += num_a
        delta = num_b - num_a
        res += min(num_b_a, delta)
        if num_b_a > delta:
            res += num_b_a - delta

    print(res)

        




if __name__ == "__main__":
    resolve()
