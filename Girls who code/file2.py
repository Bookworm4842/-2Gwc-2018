# l1 = []
# l2= [1]
# append(l2)+(l1)


# l1 = [3,8,97]
# l2 = [1,"bunny","frog","squirrel",2.9,5]
# l1.append(l2)
# # print(len(l2+l1))
# print(l2+l1)
# str = input(What do you need to buy?)
# newList = input(l1)
# l2=list[]
# newList.append(l2)
# print(l2)

# list=[6,8,3,5,9,2]
# list=["poo","amir","learning","coffee"]

# list=["poo","amir","Divya","learning","coffee"]
# print("Before:",list)
#
# #sorting numerically
# # list.sort()
# # print("After:",list)
# #weird thing: capital vs. lowercase letters
#
# for i in range(len(list)):
#     list[i].lower()
# list.sort()
# print("After:",list)

#Capital letters go before lowercase letters
#weird thing 2: sorting numbers and words
#weird thing 3: sorting lists of lists
# addy=[["weird","thing"],["number","3"],["we","will","see!"]
# print("Before:",addy)
# addy.sort()
# print("After:",addy)

# addy=[["weird","thing"],["number","3"],["we","will","see!"]
# print("Before:",addy)
# sorted(addy)
# print("After:",addy)
# my_list=[1,2,3,4,5,6,7,8,9]
# print("Before: ", my_list)
# print("test1: ",my_list[1:6])
# print("test1: ",my_list[1:6:2])
#^skips every other number


# from random import *
#
# aList=["Donkey", "Shrek", "Fiona", "Big Bad Wolf", "Dragon", "Pinnochio", "3 Blind Mice", "Lord Farquad","Charming", "Fairy godmother", "Gingerbread man" ]
#
# aRandomIndex=randint(0,len(aList)-1)
# # int=str(aRandomIndex)
# print(aList[aRandomIndex])

# aList=[5,12,3,56,24,78,1,15,44]
#
# average=(sum(aList))/(len(aList))
# print(average)

Var_correct=["v","a","r","i","a","b","l","e","s"]
numTries = 0
numFails =0
for i in range(9):
    answer = input("Guess a letter: ")
    answer = answer.lower()
    numTries += 1

    if(answer in Var_correct):
        print("That is a letter!")
    else:
    	print("Sorry, that's not a letter!")
print("The word was variables!")
numFails+=1

if (numFails == 9):
    quit()
