


# Thread Synchronization

'''
# Thread synchronization is defined as a mechanism which ensure that
two or more concurrent thread do not simultaneously execute some paraticular program
segment known as critical section 
'''

# Simple Example
'''
import threading as th


class bank:
    def __init__(self):
        self.amount = 0

    def deposit(self):
        for i in range(10000000):
            self.amount = self.amount +1

if __name__=="__main__":

    obj = bank()
    print(obj.amount)
    t1 = th.Thread(target = obj.deposit)
    t2 = th.Thread(target = obj.deposit)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(obj.amount)


'''

'''
import threading as th

balance = 0

print(balance)
def deposit():
    global balance
    for i in range(100000000):
        balance = balance + 1

if __name__=="__main__":

    t1 = th.Thread(target = deposit)
    t2 = th.Thread(target = deposit)


    t1.start()
    t2.start()


    t1.join()
    t2.join()


    print(balance)

'''
import threading as th

balance = 0

print(balance)
def deposit(lock):
    global balance
    for i in range(100000000):

        lock.acquire()
        balance = balance + 1
        lock.release()

if __name__=="__main__":

    lock = th.Lock()  # object of locak class
    
    t1 = th.Thread(target = deposit , args = (lock,))
    t2 = th.Thread(target = deposit , args = (lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print(balance)




















































