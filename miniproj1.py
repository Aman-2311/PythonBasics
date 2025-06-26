import random 
secret = random.randint(1,10)
attempts =0
while True:
 guess =int (input("Guess: "))
 attempts +=1
 if guess==secret:
   print(f"correct{attempts}attempts")
   break
 elif guess < secret:
   print("too low")
 else:
  print("too high")
