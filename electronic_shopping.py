balance=input("what is your inital balance")
st=input("What products do you want to buy, an IPhone X, a Xbox one X, an Alienware gaming laptop, or some video games")
iphonex=699.99
xbox1x=499.99
alienware17=1299.99
vidgames=32.99
if st=="iphonex":
    balance=balance-iphonex
    
elif st=="xbox1x":
    balance=balance-xbox1x
    
elif st=="alienware":
    balance=balance-aleinware
    
elif st=="vidgames":
    balance=balance-vidgames

st=input("Do you want to buy any other products, if so chose from, an IPhone X, a Xbox one X, an Alienware gaming laptop, or some video games")
if st=="iphonex":
    balance=balance-iphonex
    
elif st=="xbox1x":
    balance=balance-xbox1x
    
elif st=="alienware":
    balance=balance-aleinware
    
elif st=="vidgames":
    balance=balance-vidgames
    st=input("Do you want to buy any other products, if so chose from, an IPhone X, a Xbox one X, an Alienware gaming laptop, or some video games")
if st=="iphonex":
    balance=balance-iphonex
    
elif st=="xbox1x":
    balance=balance-xbox1x
    
elif st=="alienware":
    balance=balance-aleinware
    
elif st=="vidgames":
    balance=balance-vidgames
    st=input("Do you want to buy any other products, if so chose from, an IPhone X, a Xbox one X, an Alienware gaming laptop, or some video games")
if st=="iphonex":
    balance=balance-iphonex
    
elif st=="xbox1x":
    balance=balance-xbox1x
    
elif st=="alienware":
    balance=balance-aleinware
    
elif st=="vidgames":
    balance=balance-vidgames
if balance <=0:
    print("You do not have the amount of money required to buy these items")
elif balance >0:
    print("You have ",balance,"left in your bank account")
    
