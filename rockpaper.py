
import random


while True:
    
    computer=["rock","paper","scissors"]
    a=random.choice(computer)


    player=input("choose between rock ,paper and scissors: ")
    while player.lower() not in ["rock","paper","scissors"]:
        player=input("please put a valid option.choose between rock ,paper and scissors: ")
        if player.lower()in ["rock","paper","scissors"]:
            if player.lower()==a:
                print(player +" and "+a+" are equal so it is a tie")
            elif player.lower()=="rock":
                if a=="paper":
                    print("paper covers rock so you lose")
                else:
                    print("rocks breaks scissors so you win")
            elif player.lower()=="paper":
                if a=="rock":
                    print("paper coers rock so you win")
                else:
                    print("scissors cuts paper so you lose")
            elif player.lower()=="scissors":
                if a=="rock":
                    print("rock breaks scissors so you lose")
                else:
                    print("scissors cuts paper so you win")
        
            
            keepPlaying = input("do you want to continue?(yes or no): ").lower()
            
        
            if keepPlaying.lower()=="no":
                break





    
    