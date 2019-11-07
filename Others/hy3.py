from random import randint

def guessNumber(MaxValue=10,maxTimes=3):
    value=randint(1,MaxValue)#包含maxvalue
    for i in range(maxTimes):
        prompt="Start to guess:'if i==0 else 'Guess again:"
        try:
            x=int(input(promt))
        except:
            print("Must input an integer between 1 and ",MaxValue)
        else:
            if x==value:
                print("Congratulations")
                break
            elif x>value:
                print("Too big")
            else:
                print("too little")



    else:#跳出了for循环，有几种特殊情况
            print("Game over.FAIL.")
            print("The value is",value)

guessNumber()

                    
