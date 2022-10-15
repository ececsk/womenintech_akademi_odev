#Biz bir sayı belirleyerek bilgisayarın bu sayıyı tahmin etmesini sağlayalım.
import random

def computer_guess(x):
  start=1
  end=100
  result=""
  while result!="c":
    guess=random.randint(start,end)

    result=input(f"Is {guess} if higher than the value you have in mind (h), if lower (l), if correct (c). If you want to exit the game, press any key.\n").lower() 
    if result=="h":
      end=guess-1
    elif result=="l":
      start=guess+1
  print("Congratulations! Right guess.")
    

computer_guess(29)