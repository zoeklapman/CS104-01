#Python Queue Simulation
#19 November 2020
#Zoë Klapman
import random

first_name = ["Max", "Charlie", "Cooper", "Buddy", "Rocky", "Milo", "Jack", "Bear", "Boomer", "Tanner"]
names = []
for i in range(0,10):
    names.append(random.choice(first_name))
for i in range(0,len(names)):
    print(names.pop(0))