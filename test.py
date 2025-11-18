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

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

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


# class Hero:
#     def _init_(self, name , money ):
#         self.name=name
#         self.money=money
#     def buy(self,inventory):
#         self.inventory=inventory
def isvalid(email,password):
    if " " in email():
        return"There should be no space"
    if "@" not in email:
        return "Not valid email"
    character=len(password)
    if character < 8:
        return"You need atleast 8 characters for your"
    if password.isupper:
        return "You need a upper case"
print(isvalid("mangomustard@gmail.com","676141tungtung"))
