import random
import time

fruits = ["Apple","Banana","Grapes","Avocado"]

fruit_choice = random.choice(fruits)
random_num = random.randint(1,10)
print("Random Fruit: ", random_num)
time.sleep(5)
print("Random fruit", fruit_choice)