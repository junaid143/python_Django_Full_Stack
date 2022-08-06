

# 2 - MutiThreading 
'''
# what is thread ?

Thread in python are an entity within a process that can be schecduled for execution

# threads Execute parelly
'''
'''
# Simple Example

def squar(data):
    for i in data:
        print("Squar of the Number :",i**2)

def cube(data):
    for i in data:
        print("Cube of the Number :",i**3)

data = [2,3,4,5,6,7,8,9]

squar(data)
cube(data)










# Example with thread

import threading as th

def squar(data):
    for i in data:
        print("Squar of the Number :"+str(i**2))

def cube(data):
    for i in data:
        print("\tCube of the Number :"+str(i**3))


if __name__=="__main__":
    data = [2,3,4,5,6,7,8,9]

    # create thread 
    t1 = th.Thread(target = squar , args = (data,))
    t2 = th.Thread(target = cube , args = (data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Program Finish ")










# Example 2 with audio and video 

# Simple Example
# pip install playsound

import os
from playsound import playsound

def audio():
    playsound(r"money.mp3")


def video():
    os.system(r"minions.mp4")



audio()
video()



# Example with Thread
import threading as th

import os
from playsound import playsound

def audio():
    playsound(r"money.mp3")


def video():
    os.system(r"minions.mp4")


if __name__=="__main__":
    t1 = th.Thread(target = audio)
    t2 = th.Thread(target = video)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
'''


import threading as th

class data1:
    def squar(self,data):
        for i in data:
            print(f"squar is {i**2}\t")

    def cube(self,data):
        for i in data:
            print(f"Cube is {i**3}")


if __name__=="__main__":

    data = [2,3,4,5,6,7,8,9]
    obj = data1()

    t1 = th.Thread(target = obj.squar ,args = (data,) )
    t2 = th.Thread(target = obj.cube ,args = (data,) )

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

























