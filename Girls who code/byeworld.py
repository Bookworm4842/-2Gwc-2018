# answer = input("Pick a number between 1-10")
# newAnswer = int(answer)
# print(newAnswer)
#
# if (newAnswer > 10):
#     print("Your number is too big!")
#
# else:
# print("Your number is in the correct range!")
print("\nNow let's try it with True and break instead of a variable!")
while(True):
    name = input("What is my name?: ")
    if(name == "Ashley"):
        print("That is correct!")
    else:
        print("That's not right! Let's try something else!")
        age = input("How old am I?: ")
        newAge = int(age)
        if(newAge == 16):
            print("That is right!")
            print("You won the game!")
            break
        else:
            print("Uh oh! You got it wrong!")
            print("The game is over!")
            break
