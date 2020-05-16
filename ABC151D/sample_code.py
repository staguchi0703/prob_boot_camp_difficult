import collections
import time

start = time.time()
que = collections.deque()
for i in range(10**5):
    que.append(i)

elapsed_time = time.time() - start
print('single', elapsed_time)

start = time.time()
que = collections.deque()
for i in range(10**5):
    que.append([i,i+1])

elapsed_time = time.time() - start
print('double', elapsed_time)


start = time.time()
que = collections.deque()
for i in range(10**5):
    que.append([i, i+1, i*2])

elapsed_time = time.time() - start
print('triple', elapsed_time)