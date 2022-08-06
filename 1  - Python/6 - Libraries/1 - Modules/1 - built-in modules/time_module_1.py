import time

#print(dir(time))

#help(time.strftime)

'''
start = time.time() # capture start time

n = 5
fact = 1
for i in range(n,0,-1):
    fact = fact*i

print(fact)

end = time.time()  # capture end time 

result = (end - start)*1000 # reslt in mili seconds 
print(result)

# Example
n = 12
for i in range(1 , 11):
    time.sleep(2)
    print(n*i)

'''    
# Example
while True:
    time.sleep(1)
    t = time.strftime("%I : %M : %S %p")
    print(t)










