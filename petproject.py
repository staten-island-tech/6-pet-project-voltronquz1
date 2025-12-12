import random
class Hero:
    def _init_(self,hunger,thirst,clean,sleep,happiness,money,ap):
        self.hunger=hunger
        self.thirst=thirst
        self.clean=clean
        self.sleep=sleep
        self.happiness=happiness
        # player money
        self.money=money
        self.ap=ap
    hunger=100
    thirst=100
    clean=100
    sleep=100
    happiness=100

    #check if alive
    def alive(pet):
        pet.hunger > 0
        pet.happiness >0
        pet.clean > 0
        pet.thirst > 0
        pet.sleep > 0
    #caps stats
    def statcap(pet):
        pet.hunger=max(0,min(10,pet.hunger))
        pet.happiness=max(0,min(100,pet.happiness))
        pet.clean =max(0,min(100,pet.clean))
        pet.thirst=max(0,min(100,pet.thirst))
        pet.sleep =max(0,min(100,pet.sleep))
    happinessloss=random.randint(5,10)
    dirtyness=random.randint(5,10)
    thirstness=random.randint(5,10)
    sleepyness=random.randint(5,10)
    def game(self):
        options=[
        "Play:$10",
        "Feed:$10",
        "Hydrate:$10",
        "Clean:$10",
        "Work:$0",
        "sleep:$10"
    ]
        
        print("welcome to this ga,e")
        print(options)
        action=input(":").lower()
        for i in options:
            if "sleep" in action:
                if self.money > self.sleep:
                    print( "Need more money")
                else:
                    self.sleep+=5
            if "play" in action:
                if self.happiness  > self.money:
                    self.happiness+=5
                else:
                    print("need more money")
            if "hydrate" in action:
                if self.thirst < self.money:
                    self.thirst+=5
                else:
                    print("need more money")
            if "clean" in action:
                if self.clean < money:
                    self.play +=5
                else:
                    print("need more money")
            if "work" in action:
                money+35

            if "feed" in action:
                if self.hunger < money:
                    self.hunger+=10
                else:
                    print("need more money")
            if "sleep" in action:
                if self.play < money:
                    self.play+=5
                    money= money- self.work
                else:
                    print("need more money")
            else: 
                print("Invalid moobse")
                self.ap-=1
                if self.ap==0:
                    self.ap=3


#def _init_(self,hungrIUE,AEGAG,AEF,AGA):
    SELF.SGGGSD=GRSG