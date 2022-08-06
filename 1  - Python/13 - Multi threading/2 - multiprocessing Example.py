

# Simple Example 

'''
def squar(data):
    for i in data:
        print(i**2)

def cube(data):
    for i in data:
        print(i**3)

data = [2,3,4,5,6,7,8,9]

squar(data)
cube(data)
'''

# multiprocessing Example
# Example for multiprocessing 

import multiprocessing as pc


def squar(data):
    for i in data:
        print(i**2)

def cube(data):
    for i in data:
        print(i**3)

if __name__=="__main__":    # after the main function execution will start

    data = [2,3,4,5,6,7,8,9]
    # create process 
    p1 = pc.Process(target = squar , args = (data,))
    p2 = pc.Process(target = cube , args = (data,))

    #start process
    p1.start()
    p2.start()

    # join()
    p1.join()
    p2.join()
    



















