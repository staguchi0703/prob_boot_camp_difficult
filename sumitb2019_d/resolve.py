def resolve():
    '''
    code here
    '''
    N = int(input())
    S = input()

    cnt = 0
    for i in range(1000):
        words = '{:0>3}'.format(i)
        k = 0
        for item in S:
            if item == words[k]:
                # print(item, words[k])
                k += 1

            if k == 3:
                cnt +=1
                break

    print(cnt)



if __name__ == "__main__":
    resolve()
