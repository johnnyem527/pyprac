def fib(n):
    idx = 0
    a = 0
    b = 1
    while idx < n:
        yield b
        a, b = b, a + b
        idx += 1

# for f in fib(1):
#     print(f)

# fibon = fib(20)
# print(fibon.__next__())
# print(fibon.__next__())
# print(fibon.__next__())
# print(fibon.__next__())

from time import sleep
import random
def dummy_fib(n):
    idx = 0
    a = 0
    b = 1
    while idx < n:
        sleep_cnt = yield b
        print('let me think {0} secs'.format(sleep_cnt))
        sleep(sleep_cnt)
        a, b = b, a + b
        idx += 1

d_fib = dummy_fib(20)
# next(d_fib)相当于d_fib.send(None)
fib_result = next(d_fib)
while True:
    print(fib_result)
    try:
        # 发送随机秒数作为yield的返回值！
        fib_result = d_fib.send(random.uniform(0, 0.5))
    except StopIteration:
        break