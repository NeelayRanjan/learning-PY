import time
n=1
ar=[]
while True:
    in1=input("what is the first number you want to change, and if you want to exit type stop")
    in3=input("what is your operater, choose from, addition, substraction, multiplcation, divison, exponents, and modulus, +, -, *, /, ^, and % respectively")
    in2=input("what is the second number you want to change, and if you want to exit type stop")
    try:
        in1=int(in1)
    except:
            print(in1,"is not a number")
    try:
        in2=int(in2)
    except:
        print(in2,"is not a number")
    if in3 == "+":
        answer = in1+in2
    elif in3 == "-":
        answer = in1-in2
    elif in3 == "*":
        answer = in1*in2
    elif in3 == "/":
        answer = in1/in2
    elif in3 == "^":
        answer=in1**in2
    elif in3 == "%":
        answer=in1%in2
    else:
        print("That is not an operater, Choose from +, -, *, /")
    print(in1,in3,in2,"is equal to",answer,"\n")
    time.sleep(2)
