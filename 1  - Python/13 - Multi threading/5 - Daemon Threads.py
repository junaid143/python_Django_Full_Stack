

# Daemon Threads

'''
there are two type of threads

1 - Non-Daemon Thread
2 - Daemon Thread

The Thread which are always going to run in the background that provides supports
to main thread or non-deamon thread those background execution are considered as daemon thread
'''

# Non- daEMON tHREAD

import threading as th
import time

def thread_1():
    print("This is Non-daemon Thread")
    time.sleep(1)
    

if __name__ == "__main__":
    t = th.Thread(target = thread_1)

    # start thread
    t.start()

    t.join()
    print("main thread executed ")





import threading as th
import time

def thread_1():
    print("This is Thread")
    time.sleep(1)
    

if __name__ == "__main__":
    t = th.Thread(target = thread_1)

    t.daemon = True
    
    # start thread
    t.start()

    
    print("main thread executed ")





























