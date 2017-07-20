
t = int(input("What is the temperature outside?"))
def tempFunction():
    if t > 60 and t < 90:
        print("warm")
    elif t >= 90:
        print("hot")
    elif t < 60:
        print("chilly")
    else:
        print("please try again")
tempFunction()










