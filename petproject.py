import random
class Hero:
    def _init_(pet, hunger , happiness,clean,thirst,sleepyness):
        pet.hunger=hunger
        pet.happiness=happiness
        pet.clean=clean
        pet.thirst=thirst
        pet.sleepyness=sleepyness
    def alive(pet):
        pet.hunger > 0
        pet.happiness >0
        pet.clean > 0
        pet.thirst > 0
        pet.sleep > 0
    def statcap(pet):
        pet.hunger=max(0,min(100,pet.hunger))
        pet.happiness=max(0,min(100,pet.happiness))
        pet.clean =max(0,min(100,pet.clean))
        pet.thirst=max(0,min(100,pet.thirst))
        pet.sleep =max(0,min(100,pet.sleep))
        
    def person(self,money):
        self.money=money
    money=100
    hunger=100
    thirst=100
    clean=100
    sleep=100
    happiness=100
    ap=3
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
    action=input(":").lower()
    # for i in counter:
    #     if action:
    #         counter+=1
    #         if counter ==3:
    #             counter=0
    if "sleep" in action:
        sleep=sleep+5
    if "feed" in action:
        hunger=hunger+5
    if "hydrate":
        thirst=5+thirst
    if "clean":
        clean=clean+5
    if "work" :
        money=money+35
    if "play":
        happiness=happiness+5
    action=0
    while ap==3:
        action+=1
        ap-1
        ap=3
