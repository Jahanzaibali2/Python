# def hello_decorator(func):

#     def inner1():
#         print("Hello, this is before function execution")
#         func()

#         print("This is after function execution")
        
#     return inner1

# def function_to_be_used():
#     print("This is inside the function !!")

# function_to_be_used = hello_decorator(function_to_be_used)

# function_to_be_used()



def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))