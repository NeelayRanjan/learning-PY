# ask user to input 10 class names into a list
# sort
# print first 5 names and call it group A
# print last 5 names and call it group B
names=input("What are the 10 names of the students of the class, please add a foward slash to separate names")
names=list(names)
names.sort()
del names[0:9]
print(names[0:5], "are is group A")
print(names[5:10], "are is group B")
