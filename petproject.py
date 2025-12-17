
class hero:
    def __init__(self,hunger,thirst,clean,sleep,happiness,money):
        self.hunger=hunger
        self.thirst=thirst
        self.clean=clean
        self.sleep=sleep
        self.happiness=happiness
        # player money
        self.money=money


    #check if alive
    def alive(self):
        return (
            self.hunger > 0 and
            self.happiness >0 and
            self.clean > 0 and
            self.thirst > 0 and
            self.sleep > 0
        )
    #caps stats
    def statcap(self):
        self.hunger=max(0,min(100,self.hunger))
        self.happiness=max(0,min(100,self.happiness))
        self.clean =max(0,min(100,self.clean))
        self.thirst=max(0,min(100,self.thirst))
        self.sleep =max(0,min(100,self.sleep))
    
    
options=[
    "Play:$10",
    "Feed:$10",
    "Hydrate:$10",
    "Clean:$10",
    "Work:$0",
    "sleep:$10"
]

justin = hero(100,100,100,100,100,100)
name=input("Give me a name for pet: ")
def game():    
    while True:
        print("welcome to this game")
        print(options)
        action=input(":").lower()
        print(f"Here are your stats:\nHunger:{justin.hunger}\nHappiness:{justin.happiness}\nHere your clean:{justin.clean}:\nMoney:{justin.money}")
        if action == "play":
            if 10< justin.money:
                justin.happiness+=20
                justin.money-=10
                justin.clean-=10
                justin.hunger-=10
                justin.sleep-=10
            else:
                print("need more money")
            if action == "hydrate":
                if 10< justin.money:
                    justin.thirst+=20
                    justin.clean-=10
                    justin.sleep-=10
                    justin.hunger-=10
                    justin.money-=10
                else:
                    print("need more money")
            if action == "clean":
                if 10< justin.money:
                    justin.clean +=20
                    justin.hunger-=10
                    justin.sleep-=10
                    justin.thirst-=10
                    justin.money-=10
                else:
                    print("need more money")
            if action == "work":
                if 10< justin.money:
                    justin.money+=35
                    justin.clean-=5
                    justin.happiness-=10
                    justin.hunger-=5
                    justin.sleep-=5
                else:
                    print("need more money")

            if action == "feed":
                if 10<justin.money:
                    justin.hunger+=20
                    justin.clean-=5
                    justin.money-=10
                    justin.thirst-=5
                    justin.happiness-=5
                    justin.sleep-=5
                else:
                    print("need more money")
            if action == "feed":
                justin.sleep+=20
                justin.money-=10
                justin.hunger-=10
                justin.thirst-=10
                justin.happiness-=10
                justin.clean-=10
            else: 
                print("Invalid response")
        justin.statcap()
        if not justin.alive():
            print(f"{name} died")
            break




