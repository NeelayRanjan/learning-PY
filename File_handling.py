import time
'''file=open("example.txt",'r')
content=file.read()
#print(content)
file.seek(0)
content2=file.readlines()
content2=[i.rstrip("\n") for i in content2]
print(content2)'''
file=open("example.txt",'w')
file.write("Hello\nI wrote this text file using python\nBye")
print(file)
time.sleep(10)
