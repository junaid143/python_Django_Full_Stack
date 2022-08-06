# Example 1

'''
def smart_div(func):   #Decorator Function

    def inner(a,b):
        if a>b:
            a,b = b,a
        return func(a,b)

    return inner 

@smart_div
def div(a,b):   # original function 
    print(a/b)


    
div = smart_div(div)

div(2,4)
div(4,2)
'''


# Example 2

# practical definition
# decorator is a function which take function as a argument and return function also 
'''

def result_decor(result_function):   # 2 - user define decorator 

    def distintion(list_of_marks):  # 3 - add extra functionality ( inner function )
        
        for marks in list_of_marks:
            if marks >= 75:
                print("Distinction")

        result_function(list_of_marks)  

    return distintion
                
    
@result_decor
def result(list_of_marks):  # 1 - main function 

    for marks in list_of_marks:
        if marks >=35 :
            print("Student pass in subject ")
        else:
            print("Student Fail")
            break
    else:
        
        print("You are Pass In Exam")


marks = [45,8,75,87,96]

result(marks)

'''

# Example
# percentage programe


def per_mod(func):
    def inner(total , obtain):
        if obtain > total:
            total,obtain = obtain ,total
        
        return func(total,obtain)
    return inner


    
@per_mod
def percentage(total,obtain):
    per = obtain/total*100
    print("Percentage is "+str(round(per,2)))



percentage(374,500)






















































