#guessing game
def guessingGame():
    import random
    myNum = random.randint(1, 10)
    print("Guess my number between 1-10. Beware, you only have three chances.")
    max_guesses = 3
    guessesLeft = max_guesses

    while guessesLeft:
        guess = int(input("Take a guess:"))
        guessesLeft -= 1
        if guess == myNum:
            print("You guessed right!")
            break
        elif (guess == myNum - 1) or (guess == myNum + 1):
            print("Hot")
        elif (guess == myNum - 2) or (guess == myNum + 2):
            print("Warm")
        elif guess != myNum:
            print("Cold")
        if guessesLeft == 0:
            print("You are out of guesses. The number was", myNum)
guessingGame()

end = input("Do you want to play again?")
while end == 'yes' or end == 'yea' or end == 'y':
    guessingGame()
print("Come back and play again soon!")


