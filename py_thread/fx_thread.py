# 函数式使用线程
import threading

tickets = 1000
lock = threading.Lock()

def buy_ticket(tid):
    global lock
    global tickets
    while True:
        lock.acquire()
        if tickets != 0:
            print("线程" + tid + "：买到了第" + str(tickets) + "张票")
            tickets -= 1
            print("还剩 ：" + str(tickets) + "张票")
            # print(threading.current_thread())
        else:
            print("线程" + tid + ": 票已抢完！")
            lock.release()
            break
        lock.release()

for i in range(3):
    new_thread = threading.Thread(target=buy_ticket, args=(str(i),))
    new_thread.start()


