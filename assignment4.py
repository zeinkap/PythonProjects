#Assignment 4
def temp():
    fahrenheit= int(input("Enter temperature in fahrenheit: "))
    celsius= (fahrenheit-32) * 5/9
    print("In celsius, the temperature is:",celsius,"°C")
    print("In fahrenheit, the temperature was:",fahrenheit,"°F")
temp()
z = input("Do you want to end the program?")
while z == 'no':
    temp()
print("Have a good day!")

















