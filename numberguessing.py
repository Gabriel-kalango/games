import random

correct=random.randint(1,10)

count=1
while count <= 3:
    yourChoice=int(input("guess the right number:"))
    if yourChoice==correct:
        print("osheyy baddest")
        break
    else:
        if yourChoice!=correct and yourChoice<correct:
            print("try a number higher than you intial number")
            count+=1
        elif yourChoice!=correct and yourChoice>correct:
            print("try a number lower than you intial number")
            count+=1
if count>3:
    print("you lost")
