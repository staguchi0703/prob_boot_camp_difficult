def resolve():
    '''
    code here
    '''
    import collections
    N =int(input())
    As = [int(item) for item in input().split()]

    cnt = 0
    Bs = collections.deque()
    min1 = 1000000000000

    for i in As:
        if i < 0:
            cnt +=1
        Bs.append(abs(i))
        min1=min(min1, abs(i))
        
    if cnt % 2 ==0:
        print(sum(list(Bs)))
    else:
        print(sum(list(Bs))-min1*2)
        
if __name__ == "__main__":
    resolve()
