name=["Rohan","Alisha","Shanaya","Dhokaa"]
import random
name_list = len(name)
random_names = random.randint(0,name_list-1)
random_name = name[random_names]
print(f"{random_name} is going to buy movie tickets")