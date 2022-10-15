#Aklından bir sayı tut oyunu
from random import randint
def guess(number):
  user_number=int(input("Let's take a guess between 1 and 100: "))
  counter=0
  while number!=user_number:
    counter+=1
    if number<user_number:
      print("Sorry, take a smaller guess.")
    else:
      print("Sorry, take a bigger guess.")
    
    user_number=int(input("Please guess again! "))
  else:
    print("Congratulations! Right guess.") 
  print(f"You got it right on the {counter}. try. \n")

guess(randint(1,100))