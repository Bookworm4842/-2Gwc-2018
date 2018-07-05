#example of how to ask for user input
answer=input("What's your name")
print("Hello", answer, "nice to meet you!")

-list.sort()
    -sorting and saving the list without making a copy
    -faster
    -cannot retrieve original indexes
    -lets you be specific with sorted
        -ex: list.sort(reverse=True)
        -key (sort by lower or uppercase)

-sorted()
        -sorting the list and making a copy of the lists

-slicing lists
    -cut off certain elements from lists
    -can define a place to start and stop the slicing
    -you can also skip

-searching lists
        -Ex: list.index("blah")
        -you can find stuff in a list

-list.append() vs. list.extend()
        -.append() adds value as one element
        -.extend() adds values as indivual elements
        -list.append(["a",true]) will add as an element
        -[["a",true], something_else, another_one

-tuples
    -like a list
    -parenthesis instead of square brackets
    -unchangeable == immutable
    red=(255,0,0)
    tup=(1,2,3)
    list=[1,2,3]

Ex of how to convert an integer to a string:
from random import *

aList=["Donkey", "Shrek", "Fiona", "Big Bad Wolf", "Dragon", "Pinnochio", "3 Blind Mice", "Lord Farquad","Charming", "Fairy godmother", "Gingerbread man" ]

aRandomIndex=randint(0,len(aList)-1)
# int=str(aRandomIndex)
print(aList[aRandomIndex])
