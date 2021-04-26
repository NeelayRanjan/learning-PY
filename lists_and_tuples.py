list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2=['lists are editable','tuples are not editable']
# A list is also known as an array and store multiple pieces of data are changable, lists are defined by a pair of brackets [ ]
tuple=(1,2,3,4,5,6,7,8,9,0)
# A tuple is a list but, tuples can't be edited but lists can, tuples are defined by a pair of parentheses ( )
# A way to tell tuples and lists apart are brackets are like doors able to go in and change things at the other side
# but parentheses are like walls, not letting you pass thorugh and change thing at the other side
print(list1[2])
print(tuple[5])
# To call certain parts of a list do;
# name of list[place of item]
print(list1[0:26])
print(tuple[1:9])
# To call multiple parts of a list in a row do:
# name of list[start of part:end of part]
print(list1[-5])
print(tuple[-3])
# Instead of counting foward the computer counts backward, just add a negitive sign
print(list2[1].split() [3])
# To cut a part of a list do;
# name of list.split() [part of word]
