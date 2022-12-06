# #decorator practise
# from functools import wraps
# def print_function_data(fucntion):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f"you are calling{function.__name__}")
#         print(f"{fucntion.__doc__}")
#         print(f"{function.__name__}")
#         return fucntion(*args,**kwargs)
#     return wrapper
# @print_function_data
# def add(a,b):
#     '''this function takes two numbers as arguments and return their sum'''
#     return a+b
# print(add(2,3))

from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'executing...{function.__name__}')
        t1=time.time()
        r=function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f'this function took {total_time} seconds')
        return r
    return wrapper
@calculate_time
def sqaure_finder(n):
    return[i**2 for i in range(1,n+1)]
sqaure_finder(100)















9