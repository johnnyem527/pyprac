import threading

class TicketSeller(threading.Thread):
    tickets = 1000
    lock = threading.Lock()

    def __init__(self, tid):
        super().__init__()
        self.tid = tid

    def run(self):
        while True:
            self.lock.acquire()
            if self.tickets != 0:
                print("线程" + str(self.tid) + "：买到了第" + str(self.tickets) + "张票")
                self.tickets -= 1
                print("还剩 ：" + str(self.tickets) + "张票")
            else:
                print("线程" + str(self.tid) + ": 票已抢完！")
                self.lock.release()
                break
            self.lock.release()

if __name__ == '__main__':
    for i in range(3):
        ticket_seller = TicketSeller(i)
        ticket_seller.start()
