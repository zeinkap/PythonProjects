#Assignment 6
guesses = 0
myList = []
while guesses < 5:
  userArray1 = int(input("Type a number"))
  myList.append(userArray1)
  guesses+=1
myList.sort()
print("The numbers you typed:", myList)
print("The minimum number is:", myList[0])
myList.reverse()
print("The maximum number is:", myList[0])
