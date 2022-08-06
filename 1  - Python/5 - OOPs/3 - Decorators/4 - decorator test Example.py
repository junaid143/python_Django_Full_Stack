# Example 2


# Write a python program to find the studend pass or fail in evvery subject
# and add extra functionality if student have distinction in any subject then display


def decor_resut(result_function): # 2 - decorator function take result function as parameter

    def distinction(marks_list): # 3 - inner function for extra functionality
        for marks in marks_list:
            if marks >=75:
                print("Distinction ..")

        result_function(marks_list) #4 - calling the main function result for main functionality of the function 
    return distinction  # 5 - return extra functionality  
  

@decor_resut   # 6 - Decorator when we call the result function @decor_resut automatically add the extra functionality to the function
def result(marks_list):#1 -  main function take parameter as list []
    
    for marks in marks_list:
        if marks >= 35:
            pass
        else:
            print("Student Fail :")
            break
    else:
        print("Student Pass ")




result([50,60,45,77,85])
