investment=input("How much money do you want to invest")
investment=int(investment)
investment=investment/100
if investment<=100000:
    investment=investment*0.025/100
    print("your intrest is 2.5%" )
    print("your new investment is ",investment,"%")
elif investment>100001 and investment<=200000:
    investment=investment*0.05/100
    print("your intrest is 5%" )
    print("your new investment is ",investment,"%")
elif investment>=200001:
    investment=investment*0.1/100
    print("your intrest is 10%" )
    print("your new investment is ",investment,"%")

