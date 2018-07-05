def say_greeting():
        print("Amir is a nice name.")
def nice_name():
    print("is a pretty name.")
def ask_name():
    answer=input("Is your name Amir?")
    if answer==("yes"):
        say_greeting()
    if answer==("no"):
        answer=input("Then is it Maria?")
        if answer==("no"):
            answer=input("Then what is it?")
            print(answer, nice_name())
        if answer==("yes"):
            print("Maria is a nice name.")


print("Hello, I am Python!")
ask_name()
