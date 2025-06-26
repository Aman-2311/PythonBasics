#rock paper scissor
import random
computer_choice= random.choice(["rock","paper","scissor"])
attempts =0
while True:
 attempts+=1
 user_choice=input("enter your choice(r,p,s) : ")
 if user_choice not in ["rock","paper","scissor"]:
  print("INVALID")
  continue
 
 computer_choice=random.choice(["rock","paper","scissor"])
 attempts+=1

 if user_choice ==computer_choice:
   print("TIE")
 elif (user_choice=="rock" and computer_choice=="scissor")or\
      (user_choice=="paper" and computer_choice=="rock")or\
      (user_choice=="scisssor" and computer_choice=="paper"):
  print(f"heyhe! You Won. Computer sucks 🤣{attempts}attempts: ")
  
  break
 else:
  print("You are a loser🤦‍♂️")
  break
 play_again = input("Play again? (y/n): ").lower()
 if play_again != "y":
   print(f"Thanks for playing! Total rounds played: {attempts}")
   break
 