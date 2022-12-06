import random
no=random.randint(0,100)
g=1
user=int(input("enter a no. "))
game=False
while not game:
    if user==no:
        print("correct no.")
        game=True
    else:
        if user<no:
            print("no. is lower")
            g+=1
            user=int(input("enter no. again"))
        else:
            print("too high")
            g+=1
            user=int(input("enter no. agin"))
        