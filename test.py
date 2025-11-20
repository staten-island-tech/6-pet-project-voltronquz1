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


class Hero:
    def _init_(pet, hunger , happiness,clean,thirst,sleepyness):
        pet.hunger=hunger
        pet.happiness=happiness
        pet.clean=clean
        pet.thirst=thirst
        pet.sleepyness=sleepyness
    def buy(self,inventory,shop):
        self.inventory=inventory
        self.shop=shop
    shop={
        
    }



# def isvalid(email,password):
#     if " " in email:
#         return"There should be no space"
#     if "@" not in email:
#         return "Not valid email"
#     character=len(password)
#     if character < 8:
#         return"You need atleast 8 characters for your"
#     upper=0
#     lower=0
#     for i in password:
#         if i.upper():
#             upper+=1
#         if upper == 0:
#             return "You need a upper case letter"
#         if i.lower():
#             lower+=1
#         if lower==0:
#             return "You need a lower case letter"


    


# print(isvalid("Something1234@gmail.com","12355abc"))

