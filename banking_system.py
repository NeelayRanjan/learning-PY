rate=input("What is the rate of interest")
principle=input("What is the amount of money you are borrow")
time=input("how many years has passed")
time=int(time)
principle=int(principle)
rate=int(rate)
rate=rate/100
amount=principle*(1+rate)**time
amount=int(amount)
amount= round(amount[2])
amount=str(amount)
input("you will need to pay $"+amount)
