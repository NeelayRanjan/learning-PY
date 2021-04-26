inital = input("What is your inital balance")
inital=int(inital)
do1 = input("Press D if you want to deposit money, or press W if you want to withdraw money")
if do1== "W":
    do11=input("How much money do you want to withdraw")
    do11=int(do11)
    finalsum = inital-do11
    do11=str(do11)
    print("Your balance is", finalsum)
elif do1 == "D":
    do12=input("How much money do you want to deposit")
    do12=int(do12)
    finalsum = inital+do12
    do12=str(do12)
    print("Your balance is", finalsum)
elif do1== "w":
    print("Restart program and press capital W")
elif do1== "d":
    print("Restart program and press capital D")
else:
    print("Restart program and press W or D only")

