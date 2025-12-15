import random
class hero:
    def _init_(self,hunger,thirst,clean,sleep,happiness,money,ap):
        self.hunger=hunger
        self.thirst=thirst
        self.clean=clean
        self.sleep=sleep
        self.happiness=happiness
        # player money
        self.money=money
        self.ap=ap

    """ hunger=100
    thirst=100
    clean=100
    sleep=100
    happiness=100 """


    #check if alive
    def alive(self):
        self.hunger > 0
        self.happiness >0
        self.clean > 0
        self.thirst > 0
        self.sleep > 0
    #caps stats
    def statcap(self):
        self.hunger=max(0,min(10,self.hunger))
        self.happiness=max(0,min(100,self.happiness))
        self.clean =max(0,min(100,self.clean))
        self.thirst=max(0,min(100,self.thirst))
        self.sleep =max(0,min(100,self.sleep))
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
        while alive:
            print(options)
        print("welcome to this game")
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
kauhwreg = hero(100,100,100,100,0,0,15)