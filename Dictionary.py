#dictionarys
test={1:2,2:4,3:6,4:8,5:10}
#Deleting single dictionary
del test[5]
#Clearing dictionary
test.clear()
#Deleting comple dictionarys
del(test)
#Calling dictionarys
print(test[1])
#Splitting dictionarys

#Manipulating dictionarys
test[1] *= 3
#Looping dictionarys
for key, value in test.items():
    print(key, value)
#only keys
for key in test.keys():
    print(key)
#only values
for value in test.values():
    print(value)
#dictionarys inside dictionarys
test2 = {'test3':{'keys':'values'}}
