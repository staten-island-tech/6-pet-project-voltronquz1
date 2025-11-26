# class Calculator():
#     def add(x, y):
#         print(x + y)
#         return x + y

#     def add_many(numbers):
#         print(sum(numbers))
#         return sum(numbers)

#     def subtract(numbers):
#         return numbers

# Calculator.add(5, 6)

# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)
# Jillian = Hero("Jillian", 150, ["Potion"])
# Jillian.buy({"title": "Sword", "atk": 34})
# print(Jillian.__dict__)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")

import random
class Hero:
    def _init_(pet, hunger , happiness,clean,thirst,sleepyness):
        pet.hunger=hunger
        pet.happiness=happiness
        pet.clean=clean
        pet.thirst=thirst
        pet.sleepyness=sleepyness
    def person(self,money):
        self.money=money
    counter=0
    money=100
    hunger=100
    thirst=100
    clean=100
    sleep=100
    happiness=100
    hungerloss=random.randint(5,10)
    happinessloss=random.randint(5,10)
    dirtyness=random.randint(5,10)
    thirstness=random.randint(5,10)
    sleepyness=random.randint(5,10)
    options=[
        "Play:$10",
        "Feed:$10",
        "Hydrate:$10",
        "Clean:$10",
        "Work:$0",
    ]
    print(options)
    action=input(":")
    # for i in counter:
    #     if action:
    #         counter+=1
    #         if counter ==3:
    #             counter=0
    
    if "Sleep" or "sleep" in action:
        sleep=sleep+sleepyness
    if "Feed" or "feed" in action:
        hunger=hunger+hungerloss
    if "hydrate" or "hydrate":
        thirst=thirstness+thirst
    if "play" or "Play":
        happines=happiness+happinessloss 
    if "clean" or "Clean":
        clean=dirtyness+clean


