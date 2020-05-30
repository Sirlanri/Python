import random

#328
def born2():
    man = random.randint(32,328)
    woman = 328-man
    print(man,woman)

def four():
    choiceA = random.randint(80,160)
    choiceB = random.randint(50,120)
    choiceC = random.randint(30,50)
    choiceD = 328-choiceA-choiceB-choiceC
    print(choiceA,choiceB,choiceC,choiceD)

while 1:
    four()