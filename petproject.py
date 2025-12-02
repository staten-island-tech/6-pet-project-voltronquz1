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
        sleep=sleep+5
    if "Feed" or "feed" in action:
        hunger=hunger+5
    if "hydrate" or "hydrate":
        thirst=5+thirst
    if "clean" or "Clean":
        clean=clean+5
    if "work" or "Work":
        money=money+35
    if "play" or "Play":
        happiness=happiness+5

    