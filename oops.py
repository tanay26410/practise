#oops 

# class Person:
#     def __init__(self,first_name,_last_name,age) -> None:
#         # instance variable
#         print('init method // constructor get called')
#         self.first_name=first_name
#         self.last_name=_last_name
#         self.age=age
# p1=Person('Harshit','Mishra',20)
# # p2=Person('A','B',19) 
# print(p1.last_name)
# print(p1.first_name)
# print(p1.age,p1.age)

#oops exercise
# class Laptop:
#     def __init__(self,brand_name,modle_name,price) -> None:
#         #intance variable
#         self.brand=brand_name
#         self.modle=modle_name
#         self.price=price
#         self.laptop_name=brand_name+' '+modle_name
# p1=Laptop("dell",'vostro',70000)
# p2=Laptop('hp','pavillion',80000)
# print(p1.price,p2.price)
# print(p1.brand,p2.brand)
# print(p1.modle,p2.modle)
# print(p1.laptop_name,p2.laptop_name)



#oops instance methods


# class Person:
#     def __init__(self,first_name,_last_name,age) -> None:
#          # instance variable
#         #  print('init method // constructor get called')
#          self.first_name=first_name
#          self.last_name=_last_name
#          self.age=age
#     def full_name(self): # instance method
#         return (f'{self.first_name} {self.last_name}')
#     def is_age(self): #instance method
#         return self.age>18
# p1=Person('Harshit','Mishra',20)
# p2=Person('a','b',17)
# print(Person.full_name(p2))# print(Person.full_name(p2)) they both mean same thing.
# print(p1.full_name())
# print(p2.is_age())

#excercie 2
# class Laptop:
#     def __init__(self,brand_name,modle_name,price) -> None:
#         #intance variable
#         self.brand=brand_name
#         self.modle=modle_name
#         self.price=price
#         self.laptop_name=brand_name+' '+modle_name
#     def discount(self,per):
#         off_price=(self.price*per)/100
#         return self.price-off_price
# l1=Laptop('hp','pavillion',63000)
# l2=Laptop('apple','mac',1000000)
# print(Laptop.discount(l1,10))
# print(l2.discount(10))



#class variable
# class circle:
#     pi=3.14
#     def __init__(self,radius) -> None:
       
#         self.radius=radius
#     def circum(self):
#         return 2*circle.pi*self.radius
# c=circle(4)
# c1=circle(3)
# print(circle.circum(c1))
# print(c.circum())


# class Laptop:
#     per=50
#     def __init__(self,brand_name,modle_name,price) -> None:
#          #intance variable
#         self.brand=brand_name
#         self.modle=modle_name
#         self.price=price
#         self.laptop_name=brand_name+' '+modle_name
#     def discount(self):
#         off_price=(self.price*self.per)/100 #self is use when we have to change value for some object. 
#         return self.price-off_price 
# Laptop.per=40
# l1=Laptop('hp','pavillion',63000)
# l2=Laptop('apple','mac',1000000)
# l2.per=50
# print(Laptop.discount(l1))
# print(l2.discount())
# # print(l2.__dict__)


# excercise
# class person:
#     count_instance=0 #class variabel / class attribute
#     def __init__(self) -> None:
#         person.count_instance+=1
#         pass
# p1=person()
# p2=person()
# p3=person()
# print(person.count_instance) 


# class method
# class Person:
#     count_instance=0
#     def __init__(self,first_name,last_name,age) -> None:
#           # instance variable
#          #  print('init method // constructor get called')
#         Person.count_instance+=1
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     @classmethod
#     def sting(cls,st):
#         first,last,age=st.split(',')
#         return cls(first,last,int(age))
#     @classmethod
#     def count_instances(cls):
#         return f"You hace created {Person.count_instance} instance {cls.__name__} of person class"

#     def full_name(self): # instance method
#          return (f'{self.first_name} {self.last_name}')
#     def is_age(self): #instance method
#          return self.age>18
# p1=Person('Harshit','Mishra',20)
# p2=Person('a','b',17)
# # print(Person.full_name(p2))# print(Person.full_name(p2)) they both mean same thing.
# # print(p1.full_name())
# # print(p2.is_age())
# # print(Person.count_instances()) # at place of Perosn p1 and p2 can be placed
# p3=Person.sting('a,b,23') 
# print(p3.is_age())


#static method
# class Person:
#     count_instance=0
#     def __init__(self,first_name,last_name,age) -> None:
#           # instance variable
#          #  print('init method // constructor get called')
#         Person.count_instance+=1
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     @classmethod
#     def string(cls,st):
#         first,last,age=st.split(',')
#         return cls(first,last,int(age))
#     @classmethod
#     def count_instances(cls):
#         return f"You hace created {Person.count_instance} instance {cls.__name__} of person class"
#     @staticmethod
#     def hello():
#         print('hello , static method called')
#     def full_name(self): # instance method
#          return (f'{self.first_name} {self.last_name}')
#     def is_age(self): #instance method
#          return self.age>18
# p1=Person('Harshit','Mishra',20)
# p2=Person('a','b',17)
# # print(Person.full_name(p2))# print(Person.full_name(p2)) they both mean same thing.
# # print(p1.full_name())
# # print(p2.is_age())
# # print(Person.count_instances()) # at place of Perosn p1 and p2 can be placed
# p3=Person.string('a,b,23') 
# print(p3.is_age())
# Person.hello()


#encapsulation/abstraction/some nameing convention/name manglin
# class phone:
#     def __init__(self,brand,model_name,price) -> None:
#         self.brand=brand
#         self.model_name=model_name
#         self._price=price #__price # tell user that it is private method
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}....")
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def send_message(self):
#         pass # twilio
#_name convention to denote it is private method
#__name__ dunder or magic methods 
# phone1=phone('nokia','1100',1111)
# print(phone1._price)#__price
# print(phone1._phone__price)
# phone1._price=-1000
# print(phone1._price)
#__price will give error stating that phone object does not have
#any object name __price __price will be changed into _phone__price so that it remains in same class
#python changes __price name into _phone__price 
# print(phone1.__dict__)


#property setter decorator
# class phone:
#     def __init__(self,brand,model_name,price) -> None:
#         self.brand=brand
#         self.model_name=model_name
#         self._price=max(price,0)
#         # if price > 0:
#         #      self._price=price
#         # else:
#         #      self._price=0
#         # self.complete_specifiction=f"{brand} {model_name} and price {price}"
#     @property
#     def complete_specififcation(self):
#          return f"{self.brand} {self.model_name} and price {self._price}"
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self,new_price):
#         self._price=max(new_price,0)
#     def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#     def full_name(self):
#          return f"{self.brand} {self.model_name}"
# p1=phone('nokia','1100',1000)
# p2=phone('a','b',1)
# # print(p1.brand)
# # print(p1.model_name) 
# p1.price=-500 #--> p1.price will give -500 and p1.complete_specification will give 1000
# print(p1.price)
# print(p1.complete_specififcation)   


#inheritance

# class phone: #--> super class , base class
#      def __init__(self,brand,model_name,price) -> None:
#          self.brand=brand
#          self.model_name=model_name
#          self._price=price #__price # tell user that it is private method
#      def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#      def full_name(self):
#          return f"{self.brand} {self.model_name}"
# class smartphone(phone): #--> sub class, derived class #inheritance 
#     def __init__(self, brand, model_name, price,ram,internal_memory,rear_cam) -> None:
#         # phone.__init__(self,brand,model_name,price)
#         super().__init__(brand, model_name, price)
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_cam=rear_cam
#     def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#     def full_name(self):
#          return f"{self.brand} {self.model_name} {self._price} {self.internal_memory} {self.rear_cam}"

# p1=phone("nokia",'1100',110)
# p2=smartphone('one plus','5',3000,'4gb','64gb','20mp')
# print(p1.full_name())
# print(p2.full_name())

#multilevel inheritance mro 
# class phone:
#      def __init__(self,brand,model_name,price) -> None:
#          self.brand=brand
#          self.model_name=model_name
#          self._price=price 
#      def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#      def full_name(self):
#          return f"{self.brand} {self.model_name} {self._price}"
# class smartphone(phone):#multi level inheritance
#     def __init__(self, brand, model_name, price,ram,internal_memory,rear_cam) -> None:
#         # phone.__init__(self,brand,model_name,price)
#         super().__init__(brand, model_name, price)
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_cam=rear_cam
#     def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#     def full_name(self):#method overding
#          return f"{self.brand} {self.model_name} {self._price} {self.internal_memory} {self.rear_cam}"
# class flagshiphone(smartphone):
#     def __init__(self, brand, model_name, price,ram,internal_memory,rear_cam,front_cam) -> None:
#         # phone.__init__(self,brand,model_name,price)
#         super().__init__( brand, model_name, price,ram,internal_memory,rear_cam)
#         self.front_cam=front_cam
#     def make_a_call(self, phone_number):
#          print(f"calling {phone_number}....")
#     def full_name(self):#method overriing
#          return f"{self.brand} {self.model_name} {self._price} {self.internal_memory} {self.rear_cam} {self.front_cam}"
# p1=phone("nokia",'1100',1101)
# p2=smartphone('one plus','5',3000,'4gb','64gb','20mp')
# p3=flagshiphone('oneplus','5t',60000,'6gb','128gb','20mp','16mp')
# # print(p1.full_name())
# # print(p2.full_name())
# # print(p3.full_name())
# # print(help(flagshiphone)) #method resolution order mro
# # print(flagshiphone.mro())
# print(isinstance(p1,phone))
# print(isinstance(p3,flagshiphone))
# print(issubclass(flagshiphone,phone))


#multiple inheritance
# class a:
#     def class_a_method(self):
#         return 'class a method'
#     def hello(self):
#         return 'from class a'
# class b:
#     def class_b(self):
#         return 'class b method'
#     def hello(self):
#         return 'from class b'
# class c(b,a):
#     pass
# instance_c=c()
# # print(instance_c.class_a_method())
# # print(instance_c.hello())
# print(help(instance_c))

#special magic methods / dunder methods

class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def phone_name(self):
        return f"{self.brand} and {self.model}"

    #str ,repr
    def __str__(self): #dunder
        return f'{self.brand}  {self.price}'
    def __repr__(self):# special magic method
        return f"phone ({self.brand}, {self.model}, {self.price})"
    def __len__(self):
        return len(self.phone_name())
    def __add__(self,other):
        return  self.price+ other.price
#l=[1,2,3]
#print(l)-->[1,2,3]
p1=phone('nokia','1100',1000)
p2=phone('nokia','1100',2000)
# print((p1)) nokia  1000
# print(p1.__repr__()) phone (nokia, 1100, 1000)
# print(p1.__len__()) 14
# print(p1+p2) #3000 operating overloading, method overriding is example of polymorphism


# print(p1)--><__main__.phone object at 0x0000027DDA7CA040> 