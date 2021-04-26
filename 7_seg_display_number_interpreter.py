import numpy
import cv2
import time
numpy.seterr(over='ignore')
ask=input("What file should we use\n")
img=cv2.imread(ask ,0)
top=int(((img[0][1]) + (img[0][2]))/2)
topleft=int(((img[1][0]) + (img[2][0]))/2)
topright=int(((img[1][3]) + (img[2][3]))/2)
middle=int(((img[3][1]) + (img[3][2]))/2)
bottomright=int(((img[4][3]) + (img[5][3]))/2)
bottomleft=int(((img[4][0]) + (img[5][0]))/2)
bottom=int(((img[6][1]) + (img[6][2]))/2)

print(top,topleft,topright,middle,bottomleft,bottomright,bottom)

#9A
if top == 0 and topleft == 0 and topright == 0 and middle == 0 and bottomleft != 0 and bottomright == 0 and bottom == 0:
    print("True, 9")
#9B
elif top == 0 and topleft == 0 and topright == 0 and middle == 0 and bottomleft != 0 and bottomright == 0 and bottom != 0:
    print("True, 9")
else:
    print("False, 9")
#8
if top == 0 and topleft == 0 and topright == 0 and middle == 0 and bottomleft == 0 and bottomright == 0 and bottom == 0:
    print("True, 8")
else:
    print("False, 8")
#7
if top == 0 and topleft != 0 and topright == 0 and middle != 0 and bottomleft != 0 and bottomright == 0 and bottom != 0:
    print("True, 7")
else:
    print("False, 7")
#6
if top == 0 and topleft == 0 and topright != 0 and middle == 0 and bottomleft == 0 and bottomright == 0 and bottom == 0:
    print("True, 6")
else:
    print("False, 6")
#5
if top == 0 and topleft == 0 and topright != 0 and middle == 0 and bottomleft != 0 and bottomright == 0 and bottom == 0:
    print("True, 5")
else:
    print("False, 5")
#4
if top != 0 and topleft == 0 and topright == 0 and middle == 0 and bottomleft != 0 and bottomright == 0 and bottom != 0:
    print("True, 4")
else:
    print("False, 4")
#3
if top == 0 and topleft != 0 and topright == 0 and middle == 0 and bottomleft != 0 and bottomright == 0 and bottom == 0:
    print("True, 3")
else:
    print("False, 3")
#2
if top == 0 and topleft != 0 and topright == 0 and middle == 0 and bottomleft == 0 and bottomright != 0 and bottom == 0:
    print("True, 2")
else:
    print("False, 2")
#1
if top != 0 and topleft != 0 and topright == 0 and middle != 0 and bottomleft != 0 and bottomright == 0 and bottom != 0:
    print("True, 1")
else:
    print("False, 1")
#0
if top == 0 and topleft == 0 and topright == 0 and middle != 0 and bottomleft == 0 and bottomright == 0 and bottom == 0:
    print("True, 0")
else:
    print("False, 0")
#time.sleep(5)
