import random
print("player one enter")
a=random.randint(1,3)
b=input("player two enter:")
"s"==1
"w"==2
"g"==3
if a==1 and b=="w" :# 1 is snake
    print("player one wins")
elif a==2 and b=="g": # 2 is water
    print("player one wins")
elif a==3 and b=="s": # 3 is gun
    print("player one wins")
else:
    print("player two wins")
