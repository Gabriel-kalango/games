import random
import string
from words import words

def getword(words):
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words) 
    return word.upper()

def hangman():
    theword=getword(words)
    gameword_letter=set(theword)
    alpahbet=set(string.ascii_uppercase)
    usedletters=set()
    
    
    lives=6

    while len(gameword_letter)>0 and lives>0:
        

        print("you have ",lives," remaining and you have used up these words"," ".join(usedletters))
        blanks=[letter if letter in usedletters else "-" for letter in theword ]
        print("your current word : "," ".join(blanks) )
        used_letter=input("guess the letter of the word: ").upper()
        if used_letter in alpahbet-usedletters:
            usedletters.add(used_letter)
            
            if used_letter in gameword_letter:
                gameword_letter.remove(used_letter)
            else:
                lives-=1
            
        elif used_letter in usedletters:
            print("you have used the letter before")
       
    if lives==0:
        print("you lost, the word is ",theword)
    else:
        print(f"you got the word {theword} , nice kill")
    
hangman()