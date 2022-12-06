#errors
# def func(a):
#     if type(a)==int:
#         return a%2
#     raise TypeError('input passed is not int')
# # print(func('a')) TypeError: input passed is not int
# a=12
# print(func(a))

#not implemented error
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self): #abstract method there is not such thind as abstract method in python abstract method came from java
#         raise NotImplementedError("sound method not defined")

# class dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def sound(self):
#         return "bark"
# class cat(Animal):
#     def __init__(self,name,color) -> None:
#         super().__init__(name)
#         self.color=color
#     def sound(self):
#         return 'meow meow'

# d=dog('lab','husky')
# print(d.sound())
# d=cat('clory','black and grey')

# print(d.sound())

#error example
# class Mobile:
#     def __init__(self,name):
#             self.name=name
# class mobilestore:
#     def __init__(self):
#         self.mobiles=[]
#     def add_mobile(self,new_mobile):
#         if isinstance(new_mobile,Mobile):
#             self.mobiles.append(new_mobile)
#         else:
#             raise NameError('name provided does not exist Above class Mobile')
# one=Mobile('one plus 6')
# samsung='samsung galaxy 9'
# mob=mobilestore()
# # print(mob.mobiles)
# mob.add_mobile(one)
# mob_phone=mob.mobiles
# print(mob.mobiles[0].name)


#exception handling
# exception are error that occur during execution
#exception handling we use try except

# while True:
#     try:
#         age=int(input("enter your age:"))
#     except ValueError: # if above block statement not work then except will work, improves fucntionality of program as it is predetermined which error will occur
#         print("invalid input")
#     except:# if error produced by try is not value error then it will pass to this excpet which will give unexpected input
#             print("unexpected input")
#     else: #when use gives correct input and no exception occur then else is used 
#         print(f'user input={age}')
#         break
#     finally:
#         print('finally block')


# if age>18:
#         print("can play")
# else:
#         print('can not play')

#excercise
# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
#     except:
#         print('unexcpected error')
# print(div(10,2))
# print(div(10,0))
# print(div(10,'w'))


#custom exception are used to increase readablity of code
class name_problem(ValueError):
    pass
def vali(name):
    if len(name)<9:
        raise name_problem('name is t oo short')
a=str(input('enter your name'))
vali(a)
print(f'hello {a}')