import numpy as np
import random

def roll_dice():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  return sum([dice1,dice2])

def simulate_roll(n):
  results =np.zeros(n,dtype=int)
  for i in range(n):
      results[i] =roll_dice()
  return results

def analyze(results):
  print("\n.. Dise Roll Statistics : ")
  print(f"Mininum sum: {results.min()}")
  print(f"Maximum: {results.max()}")
  print(f"Average: {results.mean()}")

  for value in range(2,13):
    count =(results==value).sum()
    print(f"{value}  apperad {count}time(s)")


def main():
   
    try:
        n =int(input("How many times to roll the dice ?"))
        if n <= 0:
            print("⚠️ Please enter a positive number.")
            return
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        return
    rolls = simulate_roll(n)
    
    print(rolls)
    analyze(rolls)

if __name__ == "__main__":
  main()