#decorator
# function inside function
# def sq(a):
#     return a**2
# l=[1,2,3,4]
# def mymap(func,l):
#     li=[]
#     for i in l:
#         li.append(func(i))
#     return li
# print(mymap(sq,l))
#closure function or first class fucntion
# def to_pow(x):
#     def cal_pow(n):
#         print (n**x)
#     return cal_pow
# cube=to_pow(4)
# cube(2)

#this is how decoratot function work
# @ use for decorator


# def decorator_function(func):
#     def wrapper_func():
#         print('this is awesome function')
#         return func()
#     return wrapper_func()
# #this is awww
# @decorator_function #shortcut
# def func1():
#     print('this is function 1')
# func1 
# @decorator_function
# # this is awww

# def func2():
#     print('this is function 2')
# func2
# var=decorator_function(func2) 
# print(decorator_function)
# <function decorator_function at 0x0000011F71CF8040> 


# def decorator_function(func):
#     def wrapper_func(*args,**kwargs):
#         print('this is awesome function')
#         return func(*args,**kwargs)
#     return wrapper_func
# @decorator_function #shortcut
# def func1(**a):
#     print(f'this is function {a}')
# func1(a=2,d=1) 
# @decorator_function
# def func2(a,b):
#     return(a+b)
# print(func2(1,2))    



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