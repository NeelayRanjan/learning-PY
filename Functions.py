#Function
def Exponent(x,y):
    print(x**y)
#Return
def name(x,y):
    print(x+y)
    return(x+y)
name1=name("Neelay ", "Ranjan")
#Defualt Values
def pet(name, type = "dog"):
    print("Animal Type:",type)
    print("Animal Name:",name)
#Arbitrary Number of Arguments
def pizza(*toppings):
    print(toppings.len)
    print(toppings)
#Arbitrary Key,Value dictionary
def pizza(**toppings):
    print(toppings)
    return(toppings)
