

# Collect thread info
'''
#two threads are always run in our system
1-  main   #
2 - sock   #
'''

import threading as th
def squar(data):
    for i in data:
        print(f"Squar of the number is {i**2}\t")

def cube(data):
    for i in data:
        print(f"Cube of the number is {i**3}\t")

        
if __name__=="__main__":
    data = [2,3,4,5,6,7,8,9]

    
    t1 = th.Thread(target = squar , args = (data,))
    t2 = th.Thread(target = cube , args = (data,))
    

    t1.start()
    t2.start()
    #print(f"Active Count {th.active_count()}\t")
    #print(f"Enumerate Thread : {th.enumerate()}")
    print(f"Current_thread : {th.current_thread()}")


    t1.join()
    t2.join()

    #print(f"Active Count {th.active_count()}\t")
    #print(f"Enumerate Thread : {th.enumerate()}")
    print(f"Current_thread : {th.current_thread()}")




















