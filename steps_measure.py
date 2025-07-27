#steps
import data as np
user_steps = int(input("Enter the number of steps: "))
steps = np.random.choice([1,-1],size =user_steps)
position = np.cumsum(steps)

position = np.insert(position,0,0)

print(".../Random walk path")
print(position)
print(f"\n Final position after{user_steps} steps :{position[-1]}")