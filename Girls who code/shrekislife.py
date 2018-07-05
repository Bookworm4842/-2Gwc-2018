# print("\nI'll try to come up with a random number between 1-10 and you can guess it!")
# while(True):
#     integer = input("What do you think the number is?: ")
#     if(integer == "< 10"):
#         print("Sorry, it's lower than than!")
#     else:
#         print("That's not right! Let's try something else!")
#     age = input("How old am I?: ")
#     newAge = int(age)
#     if(newAge == 6):
#         print("That is right!")
#         print("You guessed it!")
#         break
#     else:
#         print("Uh oh! You got it wrong!")
#         print("The game is over!")
#         break

from random import *
#Generates a random integer.
aRandomNumber = randint(1, 20)
numTries= 3
# For Testing: print(aRandomNumber)
guess = input("Guess a number between 1 and 20 (inclusive): ")
numTries += 1
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")

else:
        guess= int(guess)

        if (aRandomNumber < guess):
            print("Sorry! It's higher than that!")

            if numTries>= 3:
                print("Sorry, you're out of tries.")
                for item in some_iterable:
                    ...
                    if break_condition():
                        break

                if (aRandomNumber==guess):

                    print("That's (suprisingly) correct!")
                    for item in some_iterable:
                        ...
                        if break_condition():
                            break

                    if (aRandomNumber > guess):
                        print("Sorry!It's lower than that!")
                        for item in some_iterable:
                            ...
                            if break_condition():
                                break 
